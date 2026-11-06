#!/usr/bin/env python3
"""Generate Portsmith component metadata and snapshot source pins from UniXNU."""
from __future__ import annotations
import tomllib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
LICENSES={
 "ArmCpu":"BSD-2-Clause-Patent","ArmDTPlatform":"BSD-2-Clause-Patent","ArmVirtPlatform":"BSD-2-Clause-Patent","DarwinBoot":"BSD-2-Clause-Patent",
 "Adreno740":"MIT","AdrenoMetal":"MIT","ShengUfs":"BSD-2-Clause","ShengHidInput":"BSD-2-Clause-Patent","ShengNovatekTouch":"Apache-2.0",
 "QcomGeniSpi":"BSD-2-Clause-Patent","GopFramebuffer":"BSD-2-Clause-Patent","SoftwareAES":"BSD-2-Clause-Patent","AppleKeyStoreState":"BSD-2-Clause-Patent",
 "RamBlock":"BSD-2-Clause-Patent","VirtioMmioBlock":"BSD-2-Clause-Patent","VirtioMmioConsole":"BSD-2-Clause-Patent","XnuPrelink":"BSD-2-Clause-Patent",
 "AdrenoPM4":"MIT","AdrenoFirmware":"BSD-2-Clause-Patent","ArmSmmu4K":"MIT","AirNir":"MIT","VerifiedRoot":"BSD-2-Clause-Patent",
 "Sm8550Platform":"BSD-2-Clause-Patent","ShengPreflight":"BSD-2-Clause-Patent","QcomBaseband":"BSD-2-Clause",
}
REFERENCE_ONLY={
 "Ath12kWifi":"No LICENSE/COPYING/NOTICE found at the pinned revision; some files have GPL-2.0 headers but the whole tree's license is unclear. Do not snapshot pending maintainer clarification and file-level review.",
 "QcaBluetooth":"Mixed per-file licensing (GPL-2.0-only, APSL-2.0, BSD-2-Clause-Patent, BSD-3-Clause) with root NOTICE; keep as reference until file-level license/provenance and compatibility review.",
}
SCOPE={"arm64":"arm64","platform":"platform","firmware":"firmware","gpu":"gpu","graphics":"graphics","board":"board","controller":"controller","display":"display","os":"os","storage":"storage","protocol":"protocol","tool":"tool","soc":"soc","modem":"modem"}
def q(v): return '"'+str(v).replace('\\','\\\\').replace('"','\\"').replace('\n','\\n')+'"'
def arr(xs): return "["+", ".join(q(x) for x in xs)+"]"
def add(lines,key,value):
 if value is None: return
 lines.append(f"{key} = {arr(value)}" if isinstance(value,list) else f"{key} = {q(value)}")
def main():
 cs=tomllib.loads((ROOT/"sources/UniXNU/components.toml").read_text())["component"]
 devices=tomllib.loads((ROOT/"sources/UniXNU/devices.toml").read_text())["device"]
 sheng_components={x for d in devices if d.get("name")=="sheng" for x in d.get("components",[])}
 imported=[]; sources=[]; credit_rows=[]
 for c in cs:
  cid=c["id"]; category=SCOPE.get(c.get("scope"),c.get("scope","other")); base=Path("components")/category/cid
  source_path=(base/"source").as_posix(); url=c["repository"]; owner=url.split("github.com/")[-1].removesuffix(".git").split("/")[0]
  lic=LICENSES.get(cid); pending=REFERENCE_ONLY.get(cid); port_ids=["sheng"] if cid in sheng_components else []
  lines=["[[component]]",f"id = {q('unixnu.'+cid)}",f"category = {q(category)}",f"media = {q(c.get('function',''))}",f"ports = {arr(port_ids)}"]
  if lic: add(lines,"source_paths",[source_path])
  for k,v in [("upstream_repository",url),("revision",c["revision"]),("upstream_path",c.get("path")),("source_owner",owner),("license",lic or "unresolved"),("license_status",("root license inspected at exact pinned revision; original LICENSE/NOTICE retained" if lic else pending)),("reuse_status",("vendored source snapshot; Portsmith compatibility not asserted" if lic else "reference-only; no source code imported until license/provenance review")),("status",("Upstream component source snapshot; license audited at exact pin; not Portsmith-qualified" if lic else pending)),("hardware",c.get("hardware",[])),("os_abi",c.get("os_abi",[])),("board_dependencies",c.get("board_dependencies",[])),("dependencies",c.get("dependencies",[])),("upstream_verified_devices",c.get("verified_devices",[])),("upstream_selected_by",port_ids)]: add(lines,k,v)
  imported.append("\n".join(lines))
  wrapper=["[component]",f"id = {q(cid)}",f"scope = {q(c.get('scope',''))}",f"kind = {q(c.get('kind',''))}",f"function = {q(c.get('function',''))}",f"repository = {q(url)}",f"revision = {q(c['revision'])}",f"upstream_path = {q(c.get('path',''))}",f"license = {q(lic or 'unresolved')}",f"reuse_status = {q('vendored upstream snapshot; review hardware scope before reuse' if lic else 'reference-only; pending license/provenance review')}"]
  for key in ("hardware","os_abi","board_dependencies","verified_devices","dependencies","source_files","runtime_identifiers","build_stage","build","outputs"): add(wrapper,key,c.get(key))
  base.mkdir(parents=True,exist_ok=True); (base/"component.toml").write_text("\n".join(wrapper)+"\n",encoding="utf-8")
  if lic:
   (base/"README.md").write_text(f"# {cid}\n\nThe complete upstream source snapshot is in [`source/`](source/) at `{c['revision']}`. Origin: {url}. `source/LICENSE` and any upstream `NOTICE`/copyright headers are retained; see `source/UPSTREAM.toml` for pin and license metadata.\n\nThe upstream catalog scopes this component to {', '.join(c.get('hardware', [])) or c.get('scope','unspecified')}. This is not a Portsmith compatibility claim; check board dependencies and OS ABI before reuse.\n",encoding="utf-8")
   sources.append(("UniXNU-component-"+cid,c["revision"],source_path,url,owner,c.get("function",""),lic))
  else:
   (base/"README.md").write_text(f"# {cid} — reference only\n\n{pending}\n\nUpstream: {url} at `{c['revision']}`. Hardware: {', '.join(c.get('hardware', [])) or 'see upstream catalog'}. No source code is imported here.\n",encoding="utf-8")
  credit_rows.append((cid,url,c["revision"],lic or "unresolved",owner))

 # Community eMMC driver from the a04br3 project, separate from the UniXNU 27-component catalog.
 cid="NativeMsdc"; base=Path("components/storage/emmc/NativeMsdc"); source_path=(base/"source").as_posix(); url="https://github.com/mouseos/NativeMsdc"; rev="e718d5d7bde7f6986cd9a7b425c82c50a4dcc3b8"; lic="BSD-2-Clause-Patent"
 lines=["[[component]]",f"id = {q('community.NativeMsdc')}",f"category = {q('storage')}",f"media = {q('MediaTek MT8167 MSDC0 eMMC block driver')}","ports = []",f"source_paths = {arr([source_path])}",f"upstream_repository = {q(url)}",f"revision = {q(rev)}",f"source_owner = {q('mouseos')}",f"license = {q(lic)}",f"license_status = {q('explicit SPDX identifier in LICENSE at pinned revision; README and its credits retained')}",f"reuse_status = {q('vendored source snapshot; MT8167-specific; upstream README says current driver is not yet booted')}",f"status = {q('Host tests/compile reported upstream; device boot not reported for current NativeMsdc revision')}",f"hardware = {arr(['MediaTek MT8167 MSDC0','eMMC','512-byte sectors'])}",f"dependencies = {arr(['XNU IOStorageFamily ABI','optional NativeRamBlock and VerifiedRoot integrations'])}","upstream_verified_devices = []","upstream_selected_by = []"]
 imported.append("\n".join(lines))
 wrapper=["[component]",f"id = {q(cid)}",f"scope = {q('storage')}",f"kind = {q('driver')}",f"function = {q('MediaTek MT8167 MSDC0 eMMC block driver')}",f"repository = {q(url)}",f"revision = {q(rev)}",f"upstream_path = {q('NativeMsdc.cpp')}",f"license = {q(lic)}",f"reuse_status = {q('vendored snapshot; MT8167 only; current code not device-booted')}",f"hardware = {arr(['MediaTek MT8167 MSDC0','eMMC'])}",f"dependencies = {arr(['XNU IOStorageFamily ABI','optional NativeRamBlock / VerifiedRoot'])}"]
 base.mkdir(parents=True,exist_ok=True); (base/"component.toml").write_text("\n".join(wrapper)+"\n",encoding="utf-8")
 (base/"README.md").write_text(f"# NativeMsdc eMMC component reference\n\nThe source snapshot is in [`source/`](source/) at `{rev}`. It retains its BSD-2-Clause-Patent license and upstream README/credits. Upstream credits include mouseos/edk2-mtk, mouseos/xnu_kernel_benesse_a04br3, and UniXNU.\n\nThis driver targets MediaTek MT8167 MSDC0, not Qualcomm SDM660 or generic eMMC/SDHCI. Its upstream README reports host compilation/tests but says the current NativeMsdc driver has not yet been booted. Do not transplant or treat this as Lavender verification.\n",encoding="utf-8")
 sources.append(("NativeMsdc",rev,source_path,url,"mouseos","MT8167 MSDC0 eMMC driver",lic)); credit_rows.append((cid,url,rev,lic,"mouseos"))
 (ROOT/"components/imported.toml").write_text("# Generated from pinned UniXNU components.toml plus the NativeMsdc eMMC reference.\n# Component copyrights/licenses remain individual; see each source/ and components/CREDITS.md.\n\n"+"\n\n".join(imported)+"\n",encoding="utf-8")
 sm=ROOT/"sources/manifest.toml"; old=sm.read_text(); marker="# BEGIN generated component source pins"
 if marker in old: old=old.split(marker)[0].rstrip()+"\n"
 block=[marker,"# Exact vendored snapshots from their individual upstream repositories; do not update without review."]
 for name,revision,path,url,owner,role,lic in sources:
  block += ["", "[[source]]",f"name = {q(name)}",f"revision = {q(revision)}",f"path = {q(path)}",f"upstream = {q(url)}",f"maintainer = {q(owner)}",f"role = {q(role)}",f"license = {q(lic)}",'license_file = "LICENSE"','upstream_file = "UPSTREAM.toml"','source_mode = "vendored-snapshot"']
 block += ["", "# END generated component source pins"]
 sm.write_text(old.rstrip()+"\n\n"+"\n".join(block)+"\n",encoding="utf-8")
 rows=["# Imported component source credits","","All snapshots retain the source repository's original `LICENSE`, copyright headers, README, and NOTICE when present. Pins are source commit IDs; the snapshots do not retain Git history. Original source READMEs and named acknowledgements remain in each tree; contributor histories are linked below.","","| Component | Upstream project / contributor history | Exact source revision | License |", "|---|---|---|---|"]
 for c,u,r,l,o in credit_rows:
  repo=u.split("github.com/")[-1].removesuffix(".git")
  rows.append(f"| `{c}` — {o} | [{u}]({u}) · [contributors](https://github.com/{repo}/graphs/contributors) | `{r}` | `{l}` |")
 rows += ["", "`Ath12kWifi` and `QcaBluetooth` are listed in `components/imported.toml` and the UniXNU catalog snapshot but not copied: Ath12kWifi has no root license and unclear overall grant; QcaBluetooth has mixed file-level licenses requiring scoped treatment. Parent UniXNU licensing is not assumed to cover either. See `LICENSE-AUDIT.md` for the audit method and details."]
 (ROOT/"components/CREDITS.md").write_text("\n".join(rows)+"\n",encoding="utf-8")
 print(f"Generated {len(imported)} component records and {len(sources)} vendored snapshot source pins.")
if __name__=="__main__": main()
