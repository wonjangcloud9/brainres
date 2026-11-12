<!-- Q: My Python script says ModuleNotFoundError: No module named 'requests'. Why? -->

`requests` isn't installed for the Python interpreter that runs your script. It's a third-party package, not part of the standard library, so each Python install or virtual environment needs its own copy.

The usual cause is a mismatch: `pip` installed it into one Python, but your script runs under another. Examples include a venv that isn't activated, Homebrew Python versus system Python, or an IDE pointing at a different interpreter.

**Fix:** install with the same interpreter that runs the script.

1. Check which Python runs the script:
   ```zsh
   which python3
   python3 -c "import sys; print(sys.executable)"
   ```
2. Install into that exact interpreter:
   ```zsh
   python3 -m pip install requests
   ```
3. Run the script with the same command, for example `python3 your_script.py`.

If step 2 fails with `error: externally-managed-environment`, your Python (common with Homebrew on macOS) blocks global installs. Use a virtual environment instead:

```zsh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install requests
python your_script.py
```

If you run the script from an IDE like VS Code, select `.venv/bin/python` as its interpreter too. Otherwise it keeps using a Python without `requests`.

Next step: run the step 1 commands and share the output if the error persists. I can also run them here if you point me to the script.
