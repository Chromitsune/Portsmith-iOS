#!/usr/bin/env python3
"""Initialize curated Portsmith sources, selected UniXNU catalog repos, or named reference-only sources.

This helper fetches pinned Git submodules only. It never recurses into nested
submodules and does not build, boot, flash, or reset a device.
"""
from __future__ import annotations
import argparse, subprocess, sys, tomllib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def run(paths:list[str])->int:
    if not paths:
        print("No eligible source submodules selected.",file=sys.stderr); return 2
    print(f"Initializing {len(paths)} pinned submodule(s), without recursive nested submodules.")
    cmd=["git","submodule","update","--init","--depth=1","--jobs=8","--",*paths]
    p=subprocess.run(cmd,cwd=ROOT)
    return p.returncode

def main()->int:
    ap=argparse.ArgumentParser(description=__doc__)
    group=ap.add_mutually_exclusive_group(required=True)
    group.add_argument("--curated",action="store_true",help="initialize source submodules referenced by Portsmith ports plus UniXNU framework")
    group.add_argument("--available",action="store_true",help="initialize all available UniXNU device catalog source submodules")
    group.add_argument("--name",action="append",help="initialize one available catalog device by record name; repeatable")
    group.add_argument("--reference",action="append",help="initialize a source marked reference_only in sources/manifest.toml; repeatable")
    a=ap.parse_args()
    manifest=tomllib.loads((ROOT/"sources/manifest.toml").read_text()).get("source",[])
    indexed={x["path"]:x for x in manifest}
    if a.curated:
        ports=[]
        for p in (ROOT/"ports").glob("*/port.toml"):
            port=tomllib.loads(p.read_text()).get("port",{})
            src=port.get("source")
            if src and not port.get("catalog_record",False) and not port.get("reference_only",False) and indexed.get(src,{}).get("source_mode","submodule")!="vendored-snapshot":ports.append(src)
        if "sources/UniXNU" in indexed: ports.append("sources/UniXNU")
        return run(sorted(set(ports)))
    if a.reference:
        requested=set(a.reference)
        refs=[s for s in manifest if s.get("reference_only") and s.get("name") in requested and s.get("source_mode","submodule")=="submodule"]
        found={s.get("name") for s in refs}
        missing=sorted(requested-found)
        if missing:
            print(f"Unknown reference-only sources: {', '.join(missing)}",file=sys.stderr);return 2
        return run(sorted(s["path"] for s in refs))
    devices=tomllib.loads((ROOT/"ports/catalog/unixnu-devices.toml").read_text()).get("device",[])
    selected=[d for d in devices if d.get("record_state")=="available" and (a.available or d.get("name") in a.name)]
    if a.name:
        requested=set(a.name); found={d.get("name") for d in devices}
        missing=sorted(requested-found)
        if missing: print(f"Unknown catalog names: {', '.join(missing)}",file=sys.stderr);return 2
    paths=[]; skipped=[]; reused=[]
    for d in selected:
        path=f"ports/{d['name']}/repo"
        if path in indexed and indexed[path].get("source_mode","submodule")=="submodule":
            paths.append(path)
            continue
        repo_url="https://github.com/"+str(d.get("repository", ""))
        existing=next((p for p,x in indexed.items() if x.get("revision")==d.get("revision") and x.get("upstream", "").removesuffix(".git").rstrip("/")==repo_url.removesuffix(".git").rstrip("/")),None)
        if existing:
            reused.append(f"{d['name']} -> {existing}")
        else:
            skipped.append(d["name"])
    if reused: print("Already present as curated source: "+", ".join(reused))
    if skipped: print(f"Metadata-only (not initialized): {', '.join(skipped)}")
    if not paths:
        print("No additional catalog submodules need initialization.")
        return 0
    return run(sorted(paths))
if __name__=="__main__":raise SystemExit(main())
