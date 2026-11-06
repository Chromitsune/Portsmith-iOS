#!/usr/bin/env python3
"""Add pinned submodule references for reachable UniXNU `available` device records.

This imports repository pointers, not source files into Portsmith's own tree.
Original code and license/notice files remain in each upstream repository. Use
--dry-run first; this helper never runs builds or touches hardware.
"""
from __future__ import annotations
import argparse, json, subprocess, sys, tomllib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
UNREACHABLE={
 "erhai-xingxing19035":"Exact pinned commit was not reachable from the public GitHub repository during audit.",
 "instantnoodlep":"Exact pinned commit was not reachable from the public GitHub repository during audit.",
 "instantnoodlep-zhangp996":"Exact pinned commit was not reachable from the public GitHub repository during audit.",
 "j716f-emptyghost":"Exact pinned commit was not reachable from the public GitHub repository during audit.",
 "picasso-suzukir1n":"Public GitHub returned Repository not found for the recorded owner/repository.",
 "sheng-ad1095445":"Public GitHub returned Repository not found for the recorded owner/repository.",
}
NO_ROOT_LICENSE={
 "alioth","alioth-taishang1024","elden","fuxi-kkkpc","gta4l-gta4lunix","hero2lte","kebab-stevedang67889","meizu21",
 "nx769j","odin","rmx3551","rmx3823","sm-t970","tb365fc","umi-jopangjovan","venus",
}
SPECIAL_LICENSE={
 "marble":("MIT (Marble-authored files/docs only)","LICENSE and LICENSING.md limit MIT to Marble-authored material; XNU/Apple, BearSSL and other upstream code keep their own terms; review file-by-file."),
 "marble-milacy":("BSD-2-Clause-Patent (root); BSD-2-Clause for ShengUfs component","Keep the separate drivers/ShengUfs/LICENSE and review component provenance."),
 "munch-erodenine":("MIT","Root LICENSE is MIT; separately licensed upstream material remains separate."),
 "odin3":("BSD-2-Clause-Patent (root); third-party terms in NOTICE.md","NOTICE identifies separately licensed OpenABL GPL-3.0-or-later (reported not redistributed), EDK2/Mu, Linux reference material and XNU patches; retain/inspect notice."),
 "pong":("BSD-2-Clause-Patent (root); see THIRD_PARTY_NOTICES.md","Notice says core/modules retain per-file/upstream licenses; Apple restore assets are fetched separately and not included."),
 "pong-agxmx666":("BSD-2-Clause-Patent (root); see THIRD_PARTY_NOTICES.md","Notice identifies HackiOS userland with its own license; preserve component-level terms."),
 "rmx1971":("GPL-2.0 text present; license scope unresolved","Root GPL v2 text does not state its scope clearly; do not reuse without maintainer clarification."),
 "ruby":("MIT for original code/docs; APSL-2.0 XNU patches","LICENSE scopes MIT to original material and excludes XNU patches; it references a NOTICE absent at the pin. Preserve/review per-file terms."),
 "starlte":("Mixed per-file licenses (MIT/BSD/GPL-2.0/Apache-2.0)","Mixed license file explicitly describes component-specific terms; firmware redistribution remains to be checked. Keep separate and do not flatten."),
 "zizhan":("BSD-2-Clause-Patent (root); per-file terms in THIRD_PARTY_NOTICES.md","NOTICE identifies third-party sources and APSL-2.0 XNU patches; preserve and review per-file terms."),
}

def q(s): return '"'+str(s).replace('\\','\\\\').replace('"','\\"').replace('\n','\\n')+'"'
def run(cmd,cwd=ROOT,check=True):
 return subprocess.run(cmd,cwd=cwd,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,check=check)
def audit_record(d):
 name=d['name']; repository=d['repository']; revision=d['revision']
 path=f"ports/{name}/repo"
 if name in UNREACHABLE:
  return {"name":name,"repository":repository,"revision":revision,"checkout":"metadata-only","license":"unresolved","license_status":UNREACHABLE[name],"source_path":None}
 if name in NO_ROOT_LICENSE:
  lic="unresolved — no root LICENSE/COPYING/NOTICE found"
  status="No root license/notice found at the pinned commit; source pointer only, no reuse permission asserted."
 elif name in SPECIAL_LICENSE:
  lic,status=SPECIAL_LICENSE[name]
 else:
  lic="BSD-2-Clause-Patent"
  status="Root LICENSE identified at the exact pinned revision; preserve all original notices and inspect per-file/transitive terms before reuse."
 return {"name":name,"repository":repository,"revision":revision,"checkout":"submodule-reference","license":lic,"license_status":status,"source_path":path}

def remove_partial(path):
 run(["git","submodule","deinit","-f","--",path],check=False)
 run(["git","rm","-f","--",path],check=False)

def import_one(d,dry):
 item=audit_record(d); name=item['name']; path=item['source_path']
 if not path:
  print(f"metadata only {name}: {item['license_status']}"); return item
 url="https://github.com/"+item["repository"]+".git"; rev=item["revision"]
 sources=tomllib.loads((ROOT/"sources/manifest.toml").read_text()).get("source",[])
 # Reuse a curated path only when the same owner/repository and exact commit
 # are already part of a hand-managed port; do not confuse catalog paths with
 # curated ones merely because they are present in the source manifest.
 reused=next((x for x in sources if not x.get("catalog_record",False) and x.get("revision")==rev and x.get("upstream","").removesuffix(".git").rstrip("/")==url.removesuffix(".git").rstrip("/")),None)
 if reused:
  item["checkout"]="existing-curated";item["source_path"]=reused["path"]
  print(f"reuse {name}: {reused['path']} at {rev}");return item
 existing=run(["git","ls-files","-s","--",path],check=False).stdout
 if existing:
  fields=existing.split()
  if len(fields)>=3 and fields[0]=="160000" and fields[1]==rev:
   item["checkout"]="already-pinned"
   print(f"already pinned {name} at {rev}"); return item
  return {**item,"checkout":"error","import_error":"Path already has a different index entry"}
 if dry:
  print(f"would add {name}: {url}@{rev} -> {path} [{item['license']}]"); return item
 target=ROOT/path
 target.parent.mkdir(parents=True,exist_ok=True)
 add=run(["git","submodule","add","--force","--depth","1",url,path],check=False)
 if add.returncode:
  remove_partial(path)
  return {**item,"checkout":"failed","import_error":add.stdout.strip()[-400:]}
 fetch=run(["git","fetch","--depth=1","origin",rev],cwd=target,check=False)
 if fetch.returncode:
  remove_partial(path)
  return {**item,"checkout":"failed","import_error":"pinned fetch failed: "+fetch.stdout.strip()[-400:]}
 checkout=run(["git","checkout","--detach",rev],cwd=target,check=False)
 if checkout.returncode:
  remove_partial(path)
  return {**item,"checkout":"failed","import_error":"pinned checkout failed: "+checkout.stdout.strip()[-400:]}
 run(["git","add","--",path])
 print(f"added {name}: {rev}")
 return item

def write_source_manifest(items):
 p=ROOT/"sources/manifest.toml"; text=p.read_text()
 begin="# BEGIN generated UniXNU available device source pins"; end="# END generated UniXNU available device source pins"
 suffix=""
 if begin in text:
  before,rest=text.split(begin,1)
  if end in rest: _,suffix=rest.split(end,1)
  text=before.rstrip()+"\n"
 block=[begin,"# External source pointers for records marked available in the pinned UniXNU catalog."]
 for x in items:
  if x.get("source_path") is None or x.get("checkout") not in ("submodule-reference","already-pinned"): continue
  if x.get("checkout")=="existing-curated": continue
  d=next(d for d in AVAILABLE if d['name']==x['name'])
  block += ["", "[[source]]",f"name = {q('UniXNU-device-'+x['name'])}",f"revision = {q(x['revision'])}",f"path = {q(x['source_path'])}",f"upstream = {q('https://github.com/'+x['repository'])}",f"maintainer = {q(x['repository'].split('/')[0])}",f"role = {q(d.get('title','')+'; upstream device catalog record '+x['name'])}",f"license = {q(x['license'])}",f"license_status = {q(x['license_status'])}","catalog_state = \"available\"","catalog_record = true"]
 block += ["",end]
 new=text.rstrip()+"\n\n"+"\n".join(block)+"\n"
 if suffix.strip(): new += "\n"+suffix.strip()+"\n"
 p.write_text(new,encoding="utf-8")

def write_audit_files(items):
 out=ROOT/"ports/catalog/available";out.mkdir(parents=True,exist_ok=True)
 (out/"audit.json").write_text(json.dumps({"source_catalog_revision":"e2fdae4312d0acc3d8a52bc457101e7918095e6a","records":items},indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
 ready=sum(x.get("checkout") in ("submodule-reference","already-pinned","existing-curated") for x in items)
 curated=sum(x.get("checkout")=="existing-curated" for x in items)
 missing=len(items)-ready
 catalog_refs=ready-curated
 root_licenses=sum(x.get("checkout") not in ("metadata-only",) and not x["license"].startswith(("unresolved — no root","GPL-2.0 text","MIT for original","Mixed per-file")) for x in items)
 no_root=sum(x["license"].startswith("unresolved — no root") for x in items)
 ambiguous=sum(x["license"].startswith(("GPL-2.0 text","MIT for original","Mixed per-file")) for x in items)
 readme=["# UniXNU available device source references","",f"The pinned UniXNU device catalog has **{len(items)}** records marked `available`; exact revision fetches succeeded for **{ready}** and **{missing}** remain metadata-only because the recorded repository/revision was inaccessible during the pinned-source audit.","",f"There are **{catalog_refs}** pinned Git submodule refs under `ports/<name>/repo`; the `sheng` record reuses the curated source at `ports/sheng/repo`. The {missing} inaccessible exact pins also have metadata-only `ports/<name>/` wrappers, with no device source checkout or feature evidence. The parent repository does not vendor these device source files. After a plain clone, initialize one source with `python3 tools/checkout-sources.py --name <record-name>` or initialize the accessible set with `python3 tools/checkout-sources.py --available` (no recursive submodule initialization).","",f"Root-license inventory: {root_licenses} repositories have an identifiable root license (some with scoped/third-party terms), {no_root} have no root license/notice, {ambiguous} have mixed or unclear scope, and {missing} pins were inaccessible. A source pointer is not permission to reuse code. Review per-file, nested-submodule, firmware and transitive terms before adapting code.","","`available` describes UniXNU port-record validation, not a successful build or boot. Source checkouts are discovery references; license status is recorded per repository below and in `sources/manifest.toml`. These generated `port.toml` wrappers are catalog-derived, not curated or verified Portsmith ports.","","See [`LICENSE-AUDIT.md`](LICENSE-AUDIT.md) for all pinned root-license and reachability findings."]
 (out/"README.md").write_text("\n".join(readme)+"\n",encoding="utf-8")
 root_licenses=sum(x.get("checkout") != "metadata-only" and not x["license"].startswith(("unresolved — no root","GPL-2.0 text","MIT for original","Mixed per-file")) for x in items)
 no_root=sum(x["license"].startswith("unresolved — no root") for x in items)
 ambiguous=sum(x["license"].startswith(("GPL-2.0 text","MIT for original","Mixed per-file")) for x in items)
 lines=["# Available-record source/license audit","", "Audit covers exact repository revisions from the UniXNU device catalog snapshot at `e2fdae4312d0acc3d8a52bc457101e7918095e6a`. It checks exact-commit reachability and root LICENSE/COPYING/NOTICE files. This is not a full file-by-file or legal audit; a root license does not automatically cover nested projects, firmware, or generated assets. The parent UniXNU license is not inherited by device repositories.","",f"Summary: {root_licenses} reachable entries have a recognizable root license (with some scoped/third-party terms), {no_root} have no root grant, {ambiguous} have mixed or unclear scope, and {sum(x.get('checkout')=='metadata-only' for x in items)} pinned entries were inaccessible. All source checkouts are Git submodule references; their code is not flattened into Portsmith.","","| Record | Pinned source | Checkout | Root license finding | Caveat |","|---|---|---|---|---|"]
 for x in items:
  repo=x['repository'];url=f"https://github.com/{repo}/tree/{x['revision']}"
  lines.append(f"| `{x['name']}` | [{repo}]({url}) @ `{x['revision']}` | {x['checkout']} | {x['license']} | {x['license_status']}"+(f" Import: {x['import_error']}" if x.get('import_error') else "")+" |")
 lines += ["", "These repositories remain submodules, not copied code. Preserve each source tree's own license and notices when browsing. Only adapt/copy files after checking the exact file-level license and provenance. No firmware was imported into Portsmith by creating these gitlinks."]
 (out/"LICENSE-AUDIT.md").write_text("\n".join(lines)+"\n",encoding="utf-8")

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--dry-run',action='store_true');ap.add_argument('--apply',action='store_true')
 a=ap.parse_args()
 data=tomllib.loads((ROOT/"ports/catalog/unixnu-devices.toml").read_text())["device"]
 global AVAILABLE;AVAILABLE=[d for d in data if d.get('record_state')=='available']
 items=[import_one(d,a.dry_run or not a.apply) for d in AVAILABLE]
 if a.apply:
  write_source_manifest(items);write_audit_files(items)
  failures=[x for x in items if x.get('checkout') in ('failed','error')]
  if failures: print(f"{len(failures)} import(s) failed; see generated audit",file=sys.stderr);return 1
  print(f"Imported {sum(x.get('checkout') in ('submodule-reference','already-pinned','existing-curated') for x in items)} available source references; {sum(x.get('source_path') is None for x in items)} remain metadata-only.")
 return 0
if __name__=='__main__':raise SystemExit(main())
