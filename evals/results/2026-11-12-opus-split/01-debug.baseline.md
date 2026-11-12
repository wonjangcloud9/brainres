<!-- Q: My Python script says ModuleNotFoundError: No module named 'requests'. Why? -->

`requests` isn't part of Python's standard library. It's a third-party package, so it has to be installed separately, and it has to be installed into **the same Python interpreter that runs your script**. This error usually comes from one of these:

1. **It was never installed.** Fix:
   ```zsh
   python3 -m pip install requests
   ```

2. **It was installed for a different Python.** This is very common on macOS, where you may have the system Python, Homebrew Python, pyenv, conda, etc. Running `pip install` can target one interpreter while `python3 script.py` runs another. Check that they match:
   ```zsh
   which python3
   python3 -m pip --version   # shows which Python this pip belongs to
   python3 -c "import requests; print(requests.__file__)"
   ```
   Using `python3 -m pip install ...` instead of bare `pip install ...` avoids this mismatch.

3. **A virtual environment isn't activated (or the wrong one is).** If you installed `requests` inside a venv, you need to activate it before running the script:
   ```zsh
   source .venv/bin/activate
   python script.py
   ```
   Your IDE (e.g., VS Code) may also be set to a different interpreter than your terminal. Check its selected interpreter.

4. **Homebrew Python blocks the install.** If `pip install` fails with `externally-managed-environment`, that's Homebrew protecting its Python. Use a virtual environment instead:
   ```zsh
   python3 -m venv .venv
   source .venv/bin/activate
   pip install requests
   ```

5. **A local file is shadowing it.** Less likely for this exact error, but a file named `requests.py` in your project folder can cause import problems with the real package. Rename it if it exists.

If you tell me the script's path and how you run it (terminal, IDE, cron, etc.), I can check your setup directly and pinpoint which of these it is.
