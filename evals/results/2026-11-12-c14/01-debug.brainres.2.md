<!-- Q: My Python script says ModuleNotFoundError: No module named 'requests'. Why? -->

The Python interpreter running your script doesn't have `requests` installed, usually because `pip` installed it into a different Python than the one running the script. On macOS this is common: `pip` and `python3` can point to different installs (system, Homebrew, pyenv, or a venv).

Install with the same interpreter that runs the script:

```
python3 -m pip install requests
```

`-m pip` ties the install to that exact `python3`. If you run the script with another command (for example `python` or a venv's Python), use that same command in place of `python3`.

To confirm the mismatch, compare these two outputs:

```
which python3
python3 -m pip --version
```

The path in the `pip --version` output should sit under the same Python as `which python3`. If it doesn't, that's the cause.

If Homebrew's Python gives an `externally-managed-environment` error, create a venv instead:

```
python3 -m venv .venv
source .venv/bin/activate
pip install requests
python your_script.py
```

If you tell me how you run the script (terminal, IDE, or a venv), I can check which interpreter it uses.
