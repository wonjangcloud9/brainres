<!-- Q: Python is slow because it's interpreted, right? -->

Partly, but "interpreted" is an oversimplification.

**What's true:** CPython compiles source to bytecode, then a virtual machine executes that bytecode instruction by instruction. Each step has overhead compared to native machine code that a CPU runs directly.

**What's missing:**

- **Dynamic typing is the bigger cost.** In `a + b`, Python must check at runtime what types `a` and `b` are, look up the right `__add__`, and handle the result. Every value is a heap-allocated object with a type pointer and refcount, so even `1 + 2` involves object manipulation. A compiled language with static types resolves this at compile time.
- **Other factors:** reference counting on every assignment, attribute lookups through dictionaries, and the GIL limiting multithreaded CPU parallelism (though free-threaded builds exist now).
- **Interpreted isn't inherently slow.** JIT-compiled implementations like PyPy and LuaJIT/V8 for JavaScript are interpreted-ish languages that run much faster, because they specialize code based on observed types. CPython has also been adding a specializing adaptive interpreter (3.11+) and an experimental JIT (3.13+), which help but are limited by the language's dynamism.
- **In practice it often doesn't matter.** NumPy, pandas, PyTorch and the like run the hot loops in C/C++/CUDA, so Python is just the orchestration layer. Slowness shows up mainly in tight pure-Python loops.

**Short version:** it's slow mostly because it's dynamically typed and highly dynamic at runtime, with bytecode interpretation being one contributing piece rather than the whole story.
