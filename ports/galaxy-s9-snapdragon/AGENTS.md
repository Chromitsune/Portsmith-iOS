# Galaxy S9 Snapdragon (`starqltechn`) port

Implementation and current status: [`repo/README.md`](repo/README.md) and [`repo/NOTES.md`](repo/NOTES.md) in the pinned `syncmodz/ios-s9` fork.

This is the Snapdragon S9 (SM-G9600/SDM845), not the Exynos S9 (`starlte`). Upstream reports iOS 16.7.16 reaching the home screen, with CPU rendering and incomplete hardware support; its persistent log ring and OrangeFox pull tool are useful references. The README explicitly reports no GPU driver. Treat all status as upstream-reported until independently checked.

Do not confuse this board with Lavender (SDM660) or use its addresses/firmware. Follow its own restore/backup instructions; no flash without explicit current authorization.
