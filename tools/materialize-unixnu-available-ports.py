#!/usr/bin/env python3
"""Generate Portsmith wrappers/README checklists for UniXNU available records."""
from __future__ import annotations
import argparse, json, sys, tomllib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
LABELS={"reported_working":"Reported working (upstream)","partial":"Partial / limited","in_progress":"Work in progress / incomplete","reported_unavailable":"Reported unavailable","not_tested":"Not tested / no comparable evidence","not_applicable":"Not applicable"}
def q(s): return '"'+str(s).replace('\\','\\\\').replace('"','\\"').replace('\n','\\n')+'"'
def arr(xs): return '['+', '.join(q(x) for x in xs)+']'
def vendor_for(title,repo):
 t=(title+' '+repo).casefold()
 for keys,v in [(('xiaomi','redmi','poco'),'Xiaomi'),(('oneplus','opd'),'OnePlus'),(('samsung','galaxy'),'Samsung'),(('google','pixel'),'Google'),(('nothing phone'),'Nothing'),(('lenovo','xiaoxin'),'Lenovo'),(('rockchip','orangepi','orange pi'),'Rockchip/Orange Pi'),(('meizu',),'Meizu'),(('realme','rmx'),'realme'),(('ayn','odin3'),'AYN'),(('benesse',),'Benesse'),(('qemu','virt'),'Virtual / QEMU')]:
  if any(k in t for k in keys): return v
 return 'Unknown / see upstream board'
def soc_vendor(soc):
 s=(soc or '').casefold()
 if s.startswith(('sm','sdm','msm')): return 'Qualcomm'
 if 'exynos' in s: return 'Samsung'
 if s.startswith('mt'): return 'MediaTek'
 if s.startswith('rk'): return 'Rockchip'
 if s.startswith(('ums','unisoc')) or 'unisoc' in s: return 'Unisoc'
 if 'qemu' in s: return 'Virtual'
 return 'Unknown'
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--check',action='store_true');args=ap.parse_args()
 devices={d['name']:d for d in tomllib.loads((ROOT/'ports/catalog/unixnu-devices.toml').read_text())['device']}
 manifest=tomllib.loads((ROOT/'sources/manifest.toml').read_text())['source']
 catalog_sources={s['name'].removeprefix('UniXNU-device-'):s for s in manifest if s.get('catalog_record')}
 audit={r['name']:r for r in json.loads((ROOT/'ports/catalog/available/audit.json').read_text())['records']}
 matrix={r['id']:r for r in json.loads((ROOT/'compatibility/ports.json').read_text())['ports']}
 feature_defs=json.loads((ROOT/'compatibility/ports.json').read_text())['features']
 mismatches=[];written=0
 for name,d in devices.items():
  if d.get('record_state')!='available': continue
  a=audit.get(name)
  if not a: continue
  src=catalog_sources.get(name)
  # The existing curated sheng folder already represents its matching catalog row.
  if not src and a.get('source_path') is not None: continue
  metadata_only=src is None
  if metadata_only and a.get('source_path') is not None: raise ValueError(f'{name}: source manifest entry missing for reachable audit record')
  if not metadata_only and a.get('source_path') != src.get('path'): raise ValueError(f'{name}: audit/source manifest path mismatch')
  row=matrix.get(name)
  if not row: raise ValueError(f'{name}: no compatibility matrix row')
  portdir=ROOT/'ports'/name
  if metadata_only:
   upstream='https://github.com/'+a['repository'];revision=a['revision'];port_path='ports/catalog'
   license_status=a.get('license_status','Source unavailable; license unresolved.')
  else:
   upstream=src['upstream'];revision=src['revision'];port_path=src['path']
   license_status=src.get('license_status',src.get('license','not recorded'))
   if not (ROOT/port_path).exists(): raise ValueError(f'{name}: source checkout missing at {port_path}')
  license_note=license_status.rstrip(' .;')
  comps=d.get('components',[])
  status=("UniXNU record marked available; exact source repository/revision was inaccessible during audit. Metadata only; no build/device support is implied." if metadata_only else "Catalog-derived UniXNU format-2 record marked available; this validates its record only, not a build/boot/device result.")
  port=["[port]",f"name = {q(name)}",f"model = {q(d.get('title',name))}",f"codename = {q(d.get('board') or name)}",f"soc = {q(d.get('soc') or 'Unspecified')}",f"source = {q(port_path)}",f"status = {q(status)}","catalog_record = true",f"catalog_format = {d.get('format',2)}",f"catalog_only = {'true' if metadata_only else 'false'}"]
  if metadata_only: port.append('source_mode = "catalog-reference"')
  hardware=["","[hardware]",f"vendor = {q(vendor_for(d.get('title',''),d.get('repository','')))}",f"soc_vendor = {q(soc_vendor(d.get('soc','')))}",f"storage = {q(row.get('storage','unknown'))}",f"gpu_family = {q('Qualcomm Adreno' if 'Adreno' in row.get('gpu','') else ('ARM Mali' if 'Mali' in row.get('gpu','') else 'Unknown'))}",f"gpu = {q(row.get('gpu','unknown'))}"]
  upstream_block=["","[upstream]",f"repository = {q(upstream)}",f"revision = {q(revision)}",f"catalog_record_state = {q('available')}",f"catalog_snapshot_revision = {q(row.get('catalog_snapshot_revision','e2fdae4312d0acc3d8a52bc457101e7918095e6a'))}",f"license_status = {q(license_status)}"]
  if metadata_only: upstream_block.append('checkout_status = "metadata-only; exact repository/revision inaccessible during audit"')
  if d.get('board'): upstream_block.append(f"board = {q(d['board'])}")
  if d.get('os_profile'): upstream_block.append(f"os_profile = {q(d['os_profile'])}")
  if comps: upstream_block.append(f"components = {arr(comps)}")
  if d.get('summary'): upstream_block.append(f"summary = {q(d['summary'])}")
  safety=["","[safety]","flash_requires_explicit_current_authorization = true","code_reuse_requires_per_repository_license_review = true"]
  porttext='\n'.join(port+hardware+upstream_block+safety)+'\n'
  if metadata_only:
   agtext=f'''# {d.get('title',name)} (`{name}`) — catalog metadata only\n\nThe pinned UniXNU record is marked `available`, but the recorded source repository/revision was inaccessible during the audit. This folder contains metadata only: no source checkout, build, boot, or feature result is available.\n\n- Recorded repository: `{upstream}`\n- Recorded revision: `{revision}`\n- License: {license_note}. It remains unresolved because the exact source was unavailable. Do not copy or adapt code without obtaining the source and reviewing its license.\n\nThe `source` field points to the local catalog snapshot, not a device repository. The linked UniXNU page is a generated view of its record and may include upstream-declared area states; because the exact repository commit was inaccessible for review, do not promote those to compatibility claims here. Keep matrix cells Not tested until exact-revision evidence is reviewed. Do not flash/reset without explicit, current authorization.\n'''
  else:
   agtext=f'''# {d.get('title',name)} (`{name}`) — catalog-derived port source\n\nThis Portsmith wrapper tracks one UniXNU format-2 device repository at [{upstream}@`{revision}`](repo/). It is a catalog-derived source entry, not a claim of Portsmith support.\n\n- Board/codename: `{d.get('board','unspecified')}`\n- SoC: `{d.get('soc','unspecified')}`\n- Catalog state: `available` means the UniXNU porting record validated at sync time; it does not establish a build, boot, or feature result.\n- License: {license_note}. Preserve the original source's license/notices; a missing or mixed grant means reference-only, not permission to copy.\n\nRead `repo/AGENTS.md` (if present), README, board and porting records, and exact source notices before adapting. Keep hardware-specific assumptions isolated. Report evidence from this exact revision; never transfer support claims from a same-board fork. Do not flash/reset without explicit, current authorization.\n'''
  lines=[]
  for f in feature_defs:
   default_detail=('Exact source repository/revision was inaccessible during audit; no compatibility evidence can be assessed.' if metadata_only else 'No comparable evidence recorded in the pinned project files.')
   cell=row.get('features',{}).get(f['id'],{'state':'not_tested','detail':default_detail})
   st=cell.get('state','not_tested');detail=cell.get('detail',default_detail)
   lines.append(f"| {f['label']} | {LABELS[st]} | {detail} |")
  ev=row.get('evidence_url',upstream)
  if metadata_only:
   source_intro=f"**Recorded upstream source:** [{upstream}@`{revision}`]({upstream}) — exact revision could not be fetched during audit; no `repo/` checkout is present. This folder contains only the catalog record."
   evidence_intro=f"The [UniXNU catalog page]({ev}) is a generated view of the pinned record and may include upstream-declared area states. Because the exact repository revision was inaccessible for review, this checklist does not promote those into compatibility claims. The `available` label validates the record only, not a Portsmith build or device result."
   compat_intro="All features remain Not tested because the pinned source repository/revision was inaccessible during audit."
  else:
   source_intro=f"**Upstream source:** [{upstream}@`{revision}`](repo/). This is a pinned source checkout corresponding to a UniXNU device-catalog record."
   evidence_intro=f"These states summarize evidence found in the pinned upstream repo; the status label is not an independent Portsmith test. A cell with no direct evidence remains Not tested. Start with the [pinned evidence file]({ev})."
   compat_intro=""
  compat_line=evidence_intro+((' '+compat_intro) if compat_intro else '')
  readme=f'''# {d.get('title',name)} (`{name}`)\n\n{source_intro}\n\n- **Board:** `{d.get('board','unspecified')}`\n- **SoC:** `{d.get('soc','unspecified')}`\n- **OS profile:** `{d.get('os_profile','not specified')}`\n- **Catalog-listed components:** {', '.join(comps) if comps else 'not specified'}\n- **Record state:** `available` (valid record snapshot only; no Portsmith device validation implied).\n- **License review:** {license_note}.\n\n## Compatibility at the pinned revision\n\n{compat_line}\n\n| Feature | Status | Evidence / limitation |\n|---|---|---|\n{chr(10).join(lines)}\n\nSee the [full Portsmith README matrix](../../README.md#compatibility-checklist) and [`AGENTS.md`](AGENTS.md).\n'''
  files={portdir/'port.toml':porttext,portdir/'AGENTS.md':agtext,portdir/'README.md':readme}
  for path,content in files.items():
   if args.check:
    if not path.is_file() or path.read_text()!=content: mismatches.append(path.relative_to(ROOT).as_posix())
   else:
    portdir.mkdir(parents=True,exist_ok=True);path.write_text(content,encoding='utf-8')
  written+=1
 if args.check:
  if mismatches: print('Catalog port wrappers are stale: '+', '.join(mismatches),file=sys.stderr);return 1
  print(f'Catalog port wrappers current: {written}')
 else: print(f'Generated Portsmith wrappers/compatibility READMEs for {written} catalog-derived records.')
 return 0
if __name__=='__main__': raise SystemExit(main())
