# NativeMsdc host-only test notes

The following host tests were run on the attached macOS/Apple Clang 17 host; no device was accessed:

- `sh source/tests/run.sh` passed directly: `NativeMsdc verified policy tests passed`.
- The upstream cache/timing/mode test scripts pass when run with a temporary local `c++` wrapper that removes Linux-only `-fno-pie`/`-no-pie` flags. The wrapper was under `/tmp` and is not part of Portsmith. Results:
  - `NativeMsdc verified cache tests passed (performance unverified)`
  - `NativeMsdc actual configure/failed-verification/refused-write invalidation passed`
  - `NativeMsdc actual timing helper passed: disabled no clock, original status, read/verify separation, cumulative metrics, wrap`
  - mode telemetry passed its gate/field/address/log-bound checks.
- Without that wrapper, the cache/timing and Python integration tests fail during compilation on Apple Clang because it treats `-no-pie` as an unused argument under `-Werror`. This is a test-runner portability issue; no upstream source was changed to hide it.

These are host tests of pure logic only. They do not establish MT8167 eMMC hardware operation, bootability, or compatibility with another controller.
