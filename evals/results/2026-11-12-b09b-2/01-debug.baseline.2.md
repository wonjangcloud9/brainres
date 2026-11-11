<!-- Q: My Python script says ModuleNotFoundError: No module named 'requests'. Why? -->

`requests` isn't a standard-library module, so it has to be installed separately. The error means the Python interpreter running your script can't find it. Usual causes:

1. **It's not installed at all.** Fix: `python3 -m pip install requests`
2. **It's installed for a different Python.** Common on macOS, where you may have system Python, Homebrew Python, pyenv, and conda side by side. `pip install` may have gone to one while `python` runs another. Using `python3 -m pip install ...` ties the install to the same interpreter you run.
3. **You're in the wrong virtual environment.** Either the venv isn't activated, or `requests` was installed outside it (or in a different venv).
4. **Your editor/IDE uses a different interpreter** than your terminal, so it works in one and fails in the other.
5. **A local file shadows it.** A file named `requests.py` (or a `requests/` folder) in your project can break the import, though that usually gives a different error, like a missing attribute.

To diagnose, run these in the same way you run your script:

```sh
which python3
python3 -c "import sys; print(sys.executable)"
python3 -m pip show requests
```

If `pip show` reports nothing, it's not installed for that interpreter. Install it with `python3 -m pip install requests`.

On Homebrew Python you may hit an "externally-managed-environment" error. In that case, create a venv:

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install requests
```

If you want, I can check your environment and script directly. Tell me how you run it (command, venv, IDE) and I'll pinpoint which case it is.
