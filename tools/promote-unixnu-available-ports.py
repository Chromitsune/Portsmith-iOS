#!/usr/bin/env python3
"""Move available UniXNU source gitlinks from the catalog nesting to ports/<name>/repo.

The catalog TOML/audit stay in ports/catalog. This only relocates Git submodule
pointers and updates audit/source paths; it does not copy or modify upstream code.
"""
from __future__ import annotations
import argparse,json,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def run(args,check=True):return subprocess.run(args,cwd=ROOT,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,check=check)
def gitlink(path):
 p=run(["git","ls-files","-s","--",path],check=False)
 for line in p.stdout.splitlines():
  meta,sep,name=line.partition("\t");fields=meta.split()
  if sep and name==path and len(fields)>=3 and fields[0]=="160000":return fields[1]
 return None
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--dry-run',action='store_true');ap.add_argument('--apply',action='store_true');args=ap.parse_args()
 audit=ROOT/'ports/catalog/available/audit.json';data=json.loads(audit.read_text());moves=[];updates=[]
 for r in data['records']:
  old=r.get('source_path')
  if not old or r.get('checkout') in ('metadata-only','existing-curated'):continue
  new=f"ports/{r['name']}/repo"
  if old==new:continue
  old_oid=gitlink(old);new_oid=gitlink(new)
  if old_oid==r['revision'] and new_oid is None:
   moves.append((r,old,new));updates.append((old,new));r['source_path']=new
  elif new_oid==r['revision'] and old_oid is None:
   updates.append((old,new));r['source_path']=new
  else:
   raise SystemExit(f"{r['name']}: expected old={old} gitlink {r['revision']} (got {old_oid}) or new={new} (got {new_oid})")
 print(f"{len(moves)} source gitlink(s) to move; {len(updates)-len(moves)} already at top-level; sheng reuses its curated path; inaccessible records stay metadata-only.")
 for r,old,new in moves:print(f"{r['name']}: {old} -> {new}")
 if args.dry_run or not args.apply:return 0
 for r,old,new in moves:
  (ROOT/new).parent.mkdir(parents=True,exist_ok=True)
  p=run(["git","mv","--",old,new],check=False)
  if p.returncode:raise SystemExit(f"git mv failed for {old}: {p.stdout}")
 # Update the source manifest, audit snapshot, and helper scripts to top-level paths.
 manifest=ROOT/'sources/manifest.toml';text=manifest.read_text()
 for old,new in updates:text=text.replace(f'path = "{old}"',f'path = "{new}"')
 # Mark available catalog refs so setup/watch tooling doesn't treat them as curated ports.
 for r in data['records']:
  path=r.get('source_path')
  if not path or r.get('checkout') in ('metadata-only','existing-curated'):continue
  pattern=f'path = "{path}"'
  pos=text.find(pattern)
  if pos>=0:
   end=text.find('\n',pos)
   following=text[end+1:end+80]
   if 'catalog_record = true' not in following:
    text=text[:end+1]+'catalog_record = true\n'+text[end+1:]
 manifest.write_text(text,encoding='utf-8')
 audit.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
 print("Moved source links; sources/manifest.toml and audit.json now use ports/<name>/repo.")
 return 0
if __name__=='__main__':raise SystemExit(main())
