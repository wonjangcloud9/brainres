<!-- Q: My Python script says ModuleNotFoundError: No module named 'requests'. Why? -->

The `requests` package isn't installed in the Python environment that's running your script. `requests` is a third-party library, not part of the standard library, so it has to be installed separately into each environment.

Common causes:

1. **It was never installed.** Fix: `python -m pip install requests`
2. **You installed it for a different Python.** `pip` and `python` may point to different interpreters (common on macOS with Homebrew, system Python, pyenv, or conda). Using `python -m pip` guarantees the install goes to the same interpreter that runs the script.
3. **Virtual environment mismatch.** You installed it globally but are running inside a venv (or the reverse). Activate the venv first (`source .venv/bin/activate`), then install.
4. **IDE or tool using a different interpreter.** VS Code, PyCharm, or a cron job may be configured with another Python than your terminal.
5. **A local file named `requests.py`** in your project can shadow the package, but that usually gives a different error (attribute errors), so it's less likely here.

To diagnose, run these in the same way you run your script:

```sh
python -c "import sys; print(sys.executable)"
python -m pip --version
python -m pip list | grep -i requests
```

If the first two paths point to the same Python and `requests` isn't listed, install it with `python -m pip install requests`. If you use `python3`, substitute that throughout.

If you'd like, I can check which interpreter and environment your script is using in this directory. Just tell me the script name or how you run it.
