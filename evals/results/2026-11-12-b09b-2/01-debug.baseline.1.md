<!-- Q: My Python script says ModuleNotFoundError: No module named 'requests'. Why? -->

`requests` isn't a standard library module, so it has to be installed separately, and the Python interpreter running your script doesn't have it. The usual causes:

1. **It was never installed.** Fix: `python3 -m pip install requests`
2. **It's installed for a different Python.** Common on macOS, where `pip` may point at one interpreter (Homebrew, system, pyenv, conda) and `python`/`python3` at another. Using `python3 -m pip install ...` guarantees the package goes to the same interpreter you run.
3. **You're in (or out of) a virtual environment.** If you installed it globally but run the script inside a venv (or the reverse), the venv can't see it. Activate the right one with `source .venv/bin/activate`, then install.
4. **Your editor/IDE uses a different interpreter** than your terminal. Check the selected interpreter in VS Code or PyCharm.
5. **A local file named `requests.py`** (or a `requests/` folder) in your project can shadow the real package. That usually causes a different error (missing attributes), but it's worth checking.

To diagnose, run these in the same way you run your script:

```
which python3
python3 -c "import sys; print(sys.executable)"
python3 -m pip --version
python3 -m pip show requests
```

If `pip show` prints nothing, it isn't installed for that interpreter. If the paths differ between `pip` and `python3`, that's the mismatch.

If you'd like, I can run these checks here and look at your script and environment to pinpoint which case it is.
