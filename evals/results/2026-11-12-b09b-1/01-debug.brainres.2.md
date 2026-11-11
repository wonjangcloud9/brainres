<!-- Q: My Python script says ModuleNotFoundError: No module named 'requests'. Why? -->

Because the Python interpreter running your script doesn't have `requests` installed. It's a third-party package, not part of the standard library, and it's installed per interpreter or virtual environment. The usual cause (~80% likely) is that `pip` installed it into a different Python than the one running your script.

To check, run these two commands in the same terminal you use for the script:

```
python3 -c "import sys; print(sys.executable)"
python3 -m pip --version
```

If the pip path doesn't belong to the same Python, that's the mismatch. The fix is to always install through the interpreter you run:

```
python3 -m pip install requests
```

If you use a virtual environment, activate it first (`source .venv/bin/activate`), then run the same command. On macOS with Homebrew Python, a bare `pip install` may fail with an "externally-managed-environment" error, so a venv is the clean fix: `python3 -m venv .venv`.

Also check whether your editor or IDE runs a different interpreter than your terminal, since that causes the same error.

Next step: run the first command and tell me the output if `python3 -m pip install requests` doesn't fix it.
