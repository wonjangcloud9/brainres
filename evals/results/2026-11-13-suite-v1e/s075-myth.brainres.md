<!-- Q: Python is slow because it's interpreted, right? -->

Partly, but "interpreted" is only half the story: the bigger causes are dynamic typing and how CPython runs each operation.

Interpretation itself isn't the problem, because Java and JavaScript also run on a VM and are often 10-100x faster than CPython. The real costs are:

1. **Dynamic types.** In `a + b`, CPython must look up the types of `a` and `b` at runtime, then find the right `__add__`. A compiled language knows at compile time that both are ints.
2. **Boxed objects.** Every int is a heap object with a refcount and type pointer, so `1 + 2` allocates and touches much more memory than a single CPU add.
3. **No JIT by default.** PyPy, V8 and the JVM watch hot code and compile it to machine code, specializing for the types they see. CPython 3.11+ has an adaptive interpreter that helps, and an experimental JIT exists, but neither matches a mature JIT yet.
4. **The GIL.** Threads can't run Python bytecode in parallel in the standard build. Free-threaded builds exist from 3.13, but they are not the default.

So the fair summary is: Python is slow because its semantics are very dynamic and CPython doesn't optimize them away, not simply because it is interpreted.

If you have a slow script, tell me what it does and I can profile it. Usually NumPy, `multiprocessing`, or moving one hot loop to a compiled extension fixes it.
