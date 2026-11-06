#!/usr/bin/env python3
"""Report newer upstream commits; never modify feature compatibility statuses."""
from __future__ import annotations
import argparse, json, os, subprocess, sys, urllib.error, urllib.parse, urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
API="https://api.github.com"
COMPAT_NAMES=("readme.md","notes.md","porting.toml","device.toml","devices.toml","components.toml","compatibility.json","compatibility.yml","compatibility.yaml","status.toml","status.json")
def github_repo(url:str)->str|None:
 p=urllib.parse.urlparse(url)
 if p.netloc.lower() not in ("github.com","www.github.com"): return None
 return p.path.strip("/").removesuffix(".git")
def query_remote(url:str, branch:str|None)->str:
 ref=f"refs/heads/{branch}" if branch else "HEAD"
 p=subprocess.run(["git","ls-remote","--exit-code",url,ref],text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=45)
 if p.returncode: raise RuntimeError(p.stderr.strip() or f"git ls-remote returned {p.returncode}")
 fields=p.stdout.split()
 if not fields: raise RuntimeError(f"no remote ref found for {ref}")
 return fields[0]
def compare_files(repo:str, base:str, head:str)->dict:
 out={"status":"not-queried","compatibility_files":[]}
 url=f"{API}/repos/{repo}/compare/{base}...{head}"
 headers={"User-Agent":"Portsmith-iOS-upstream-watch","Accept":"application/vnd.github+json"}
 token=os.environ.get("GITHUB_TOKEN")
 if token: headers["Authorization"]="Bearer "+token
 try:
  req=urllib.request.Request(url,headers=headers)
  with urllib.request.urlopen(req,timeout=30) as resp: payload=json.load(resp)
  files=payload.get("files",[])
  changed=[x.get("filename","") for x in files]
  matches=[]
  for f in changed:
   low=f.lower(); base_name=low.rsplit("/",1)[-1]
   if base_name in COMPAT_NAMES or "/reports/" in "/"+low or low.startswith("docs/"):
    matches.append(f)
  out={"status":"compared","ahead_by":payload.get("ahead_by"),"changed_files":len(changed),"compatibility_files":sorted(set(matches))}
 except Exception as e:
  # GitHub compare can transiently truncate a large diff (http.client.IncompleteRead).
  # Preserve the upstream head/compare link and flag the diff scan as unavailable.
  out={"status":"unavailable","detail":str(e)[:240],"compatibility_files":[]}
 return out

def main()->int:
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument("--output",type=Path,help="write stable JSON report to this path")
 ap.add_argument("--no-compare-api",action="store_true",help="skip GitHub compare API and only check remote refs")
 args=ap.parse_args()
 import tomllib
 with (ROOT/"sources/manifest.toml").open('rb') as f: srcs=tomllib.load(f).get("source",[])
 managed_paths={tomllib.loads(p.read_text()).get("port",{}).get("source") for p in (ROOT/"ports").glob("*/port.toml")}
 watched=[]; errors=[]
 for s in srcs:
  path=s.get("path","")
  # The compatibility watch follows Portsmith-managed ports/framework only;
  # the 79 discovery-only catalog checkouts are not feature-status claims.
  if path not in managed_paths and path!="sources/UniXNU": continue
  if s.get("source_mode")=="vendored-snapshot": continue
  url=s.get("upstream")
  if not url: continue
  branch=s.get("branch")
  pin=s.get("revision","")
  entry={"path":path,"repository":url,"branch":branch or "remote HEAD","pinned_revision":pin}
  try:
   head=query_remote(url,branch)
   entry["remote_head"]=head
   entry["state"]="pin-current" if head==pin else "review-required"
   repo=github_repo(url)
   if head!=pin:
    entry["compare_url"]=(f"https://github.com/{repo}/compare/{pin}...{head}" if repo else None)
    entry["compare"]=(compare_files(repo,pin,head) if repo and not args.no_compare_api else {"status":"skipped","compatibility_files":[]})
   watched.append(entry)
  except Exception as e:
   errors.append(f"{path}: {e}")
 if errors:
  for e in errors: print("ERROR: "+e,file=sys.stderr)
  return 1
 report={"schema_version":1,"purpose":"upstream source-change review only; compatibility states are never changed by this report","sources":sorted(watched,key=lambda x:x["path"])}
 text=json.dumps(report,indent=2,sort_keys=True)+"\n"
 if args.output:
  out=args.output if args.output.is_absolute() else ROOT/args.output
  out.parent.mkdir(parents=True,exist_ok=True);out.write_text(text,encoding="utf-8")
  print(f"Wrote {out.relative_to(ROOT)}; {sum(x['state']=='review-required' for x in watched)} source(s) need review")
 else: sys.stdout.write(text)
 return 0
if __name__=="__main__": raise SystemExit(main())
