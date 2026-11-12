<!-- Q: My Python script says ModuleNotFoundError: No module named 'requests'. Why? -->

The Python that runs your script doesn't have `requests` installed. It's usually installed for a different Python than the one running the script.

Two common causes:

1. **Never installed.** `requests` isn't in the standard library, so it needs `pip install requests`.
2. **Wrong interpreter.** `pip` and `python` point at different installs, for example a system Python, a Homebrew Python, or a virtualenv you haven't activated.

To check which case you have, run this:

```
python3 -c "import sys; print(sys.executable)"
python3 -m pip --version
```

Then install into that exact interpreter:

```
python3 -m pip install requests
```

Using `python3 -m pip` instead of bare `pip` ties the install to the interpreter that runs your script. If you use a virtualenv, activate it first (`source .venv/bin/activate`). In an IDE, also check that it's set to the same interpreter.

On macOS, Homebrew Python may refuse the install with an "externally-managed-environment" error. If that happens, create a venv (`python3 -m venv .venv`), activate it, and run the install there.

If it still fails, send me the output of the two check commands and I'll pinpoint the mismatch.
