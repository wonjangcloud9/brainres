<!-- Q: My Python script says ModuleNotFoundError: No module named 'requests'. Why? -->

Because the Python interpreter running your script doesn't have `requests` installed. It's a third-party package, not part of the standard library, and each Python install or virtual environment has its own set of packages.

The usual cause on macOS is a mismatch: you installed it with one `pip` but run the script with a different `python`. To check and fix it:

1. Find which interpreter runs your script: `python3 -c "import sys; print(sys.executable)"`
2. Install into that exact interpreter: `python3 -m pip install requests`
3. Re-run the script with the same `python3`.

Using `python3 -m pip` instead of bare `pip` guarantees the package goes to the interpreter you named.

If you use a virtual environment, activate it first (`source .venv/bin/activate`), then run step 2. If the install fails with "externally-managed-environment" (common with Homebrew Python), create a venv instead: `python3 -m venv .venv && source .venv/bin/activate && pip install requests`.

Want me to check which interpreter your script uses and run the install for you?
