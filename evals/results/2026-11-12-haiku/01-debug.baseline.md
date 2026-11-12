<!-- Q: My Python script says ModuleNotFoundError: No module named 'requests'. Why? -->

`requests` is a third-party package, not part of Python's standard library. The error means the Python that ran your script can't find it, usually because it was never installed for that interpreter.

**Fix:** install it with the same Python that runs your script:

```bash
python3 -m pip install requests
```

Using `python3 -m pip` rather than plain `pip` matters because it guarantees the package goes into the interpreter you're actually running. A bare `pip` may belong to a different Python install.

**Check which Python is running:**

```bash
which python3
python3 --version
python3 -c "import requests; print(requests.__file__)"
```

If the last command still fails after installing, you're probably running a different interpreter than you installed to. Common causes:

- **Multiple Pythons:** Homebrew, python.org, and the system Python can each have separate package sets. Run `python3 -m pip install requests` using the same `python3` that runs the script.
- **Virtual environment:** If you use a venv, activate it (`source venv/bin/activate`) before installing and running.
- **IDE or run configuration:** Your editor may use a different interpreter. Check its Python interpreter setting.

If you paste the full command you use to run the script and the output of the `which python3` check, I can tell you which of these applies.
