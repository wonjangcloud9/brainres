About 64% of runs will fail. That is nearly 2 in 3, even though each test fails only 2% of the time.

A run passes only if all 50 tests pass. The chance of that is 0.98 to the power of 50, about 0.36, so 36 of 100 runs pass and 64 fail.

| Flaky tests (2% each) | Runs that fail |
|---:|---:|
| 1 | 2 in 100 |
| 10 | 18 in 100 |
| 25 | 40 in 100 |
| 50 | 64 in 100 |

This assumes the flakes are independent. If many share one cause, such as a slow test database, fixing that cause fixes them all at once.

Next step: rank tests by failure count over the last 100 runs and fix the top 25 first. That alone drops failed runs from 64 to 40 in 100.
