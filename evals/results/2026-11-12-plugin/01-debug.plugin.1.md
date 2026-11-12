<!-- Q: My Python script says ModuleNotFoundError: No module named 'requests'. Why? -->

The Python interpreter running your script doesn't have `requests` installed. It's a third-party package, not part of the standard library.

The usual cause is a mismatch: `pip` installed it for one Python, but your script runs under another (system Python vs. a venv, or Homebrew vs. python.org). Installing through the interpreter itself avoids that:

```
python3 -m pip install requests
```

Run your script with the same `python3`. To check which interpreter you're using:

```
python3 -c "import sys; print(sys.executable)"
python3 -m pip --version
```

The two paths should point to the same install. If you see `externally-managed-environment` on macOS, Homebrew's Python is blocking global installs. Create a venv first:

```
python3 -m venv .venv
source .venv/bin/activate
pip install requests
```

If the error persists after this, send me the output of the two check commands above.
