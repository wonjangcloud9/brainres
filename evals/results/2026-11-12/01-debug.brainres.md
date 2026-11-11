<!-- Q: My Python script says ModuleNotFoundError: No module named 'requests'. Why? -->

Yes, `requests` isn't installed in the Python environment that runs your script. It's a third-party package, not part of the standard library, so each interpreter or virtualenv needs its own copy.

The usual cause is a mismatch: you installed it with one `pip` but run the script with a different `python`. On macOS this is common because system Python, Homebrew Python, and venvs all coexist. Your working directory looks like a temp venv path (`tmpvenvbcr1`), so the active venv may simply be a fresh one without it.

To fix it, install with the same interpreter that runs the script:

```
python -m pip install requests
```

Using `python -m pip` ties the install to that exact `python`. If you run the script with `python3`, use `python3 -m pip install requests` instead.

To confirm which interpreter you're using, run:

```
which python
python -c "import sys; print(sys.executable)"
```

If the path isn't the venv or Python you expected, activate the right venv (`source <venv>/bin/activate`) and reinstall. I can check your environment and run the install for you if you'd like.
