<!-- Q: My Python script says ModuleNotFoundError: No module named 'requests'. Why? -->

`requests` isn't installed for the Python interpreter that runs your script. It's a third-party package, not part of the standard library, so each Python install or virtual environment needs its own copy.

On macOS this often happens even after you've run `pip install requests`. You can have several Pythons (system, Homebrew, python.org, pyenv, a venv), and `pip` may belong to a different one than `python3`.

**Fix:** install with the same interpreter you run the script with:

```bash
python3 -m pip install requests
python3 your_script.py
```

`python3 -m pip` guarantees pip installs into the interpreter you call. If you run the script some other way (e.g. `python`, a venv, or an IDE's selected interpreter), substitute that command.

**Check for a mismatch:**

```bash
which python3
python3 -m pip --version   # shows which Python this pip belongs to
pip --version              # if this path differs, that's the cause
```

**If pip refuses** with `error: externally-managed-environment` (common with Homebrew Python), use a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install requests
python your_script.py
```

Run `python3 -m pip install requests`, then rerun your script. If it still fails, paste the output of the check commands and I'll find the mismatch.
