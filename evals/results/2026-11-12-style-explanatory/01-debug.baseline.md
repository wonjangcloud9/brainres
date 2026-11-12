<!-- Q: My Python script says ModuleNotFoundError: No module named 'requests'. Why? -->

`requests` isn't a standard-library module, so it has to be installed separately. The error means the Python interpreter running your script can't find it in its `site-packages`. This usually happens for one of these reasons:

1. **It was never installed.** Fix with `python3 -m pip install requests`.
2. **It's installed for a different Python.** This is the most common cause on macOS. `pip` may belong to one interpreter (Homebrew, system, pyenv, conda) while `python` runs another.
3. **You're in the wrong virtual environment**, or you created a venv but didn't activate it (`source .venv/bin/activate`).
4. **Your IDE or tool uses a different interpreter** than your terminal (VS Code, PyCharm, cron, etc.).

`★ Insight ─────────────────────────────────────`
- Use `python3 -m pip install ...` instead of bare `pip install ...`. The `-m` form guarantees pip is tied to the same interpreter that will run your script.
- Each Python installation and virtual environment has its own isolated `site-packages`. Packages installed in one are invisible to the others.
- On recent macOS and Homebrew Python, installing into the global environment is often blocked (PEP 668, "externally-managed-environment"). A virtual environment is the intended workaround.
`─────────────────────────────────────────────────`

To diagnose, run these in the same terminal you use to run the script:

```bash
which python3
python3 -c "import sys; print(sys.executable)"
python3 -m pip --version
python3 -m pip show requests
```

If `pip show requests` prints nothing, it isn't installed for that interpreter. The recommended fix is a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install requests
python your_script.py
```

If you share the output of the diagnostic commands and how you're running the script (terminal, IDE, etc.), I can pinpoint which case you're in.
