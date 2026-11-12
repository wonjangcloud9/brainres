<!-- Q: Should I learn Rust or Go next? -->

Learn Go next unless you need systems-level work, because it takes weeks to be productive in Go and months in Rust.

| | Go | Rust |
|---|---|---|
| Time to productive | 2-4 weeks | 2-4 months (ownership and lifetimes are the hurdle) |
| Best for | Backend services, CLIs, cloud/DevOps tooling | Systems, embedded, game engines, WebAssembly, perf-critical code |
| Concurrency | Goroutines and channels, simple | Safe but more complex (async, `Send`/`Sync`) |
| Teaches you | Pragmatic simplicity | Memory and ownership, which carries over to C/C++ |

Choose Rust instead if you work close to hardware, need no garbage-collector pauses, or want the concepts for their own sake.

I don't know your background or goals, so this is the general default. If you tell me what you build (or want to build) and which languages you already know, I can make the pick firmer and suggest a first project.
