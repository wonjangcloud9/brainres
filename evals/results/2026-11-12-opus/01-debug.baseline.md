<!-- Q: My Python script says ModuleNotFoundError: No module named 'requests'. Why? -->

`requests` is a third-party package, not part of Python's standard library, so it has to be installed separately. The error means the Python interpreter running your script can't find it. There are two common causes.

**1. It isn't installed at all.** Install it:

```bash
python3 -m pip install requests
```

**2. It's installed, but for a different Python.** This is very common on macOS, where you might have the system Python, a Homebrew Python, pyenv, conda, or a virtualenv side by side. `pip install` may have put `requests` into one interpreter while your script runs with another.

To check, compare these:

```bash
which python3                      # the interpreter your shell uses
python3 -m pip show requests       # is requests installed for *that* interpreter?
head -1 your_script.py             # a shebang line may point to a different Python
```

**Fixes:**

- **Use `python3 -m pip`** instead of bare `pip`. It installs into the same interpreter you'll run the script with.
- **If you use a virtualenv**, activate it first (`source .venv/bin/activate`), then install and run inside it.
- **If you run the script from an IDE** (VS Code, PyCharm), check which interpreter it's set to. It's often different from your terminal's.
- **If you get an `externally-managed-environment` error** (Homebrew Python does this), create a virtualenv:
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  pip install requests
  ```

If you tell me the script's path and how you're running it, I can check which interpreter it's using and whether `requests` is installed there.
