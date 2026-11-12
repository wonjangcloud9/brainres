<!-- Q: My Python script says ModuleNotFoundError: No module named 'requests'. Why? -->

Python can't find `requests` because the interpreter running your script doesn't have it installed. The usual cause is that `pip` installed it into a different Python than the one running your script. I haven't seen your script or environment, so this is the likely cause, not a confirmed one.

`★ Insight ─────────────────────────────────────`
- Each Python install or virtual environment has its own `site-packages`. `pip` and `python` on your `PATH` can point to different ones, which is common on macOS with system, Homebrew, and pyenv Pythons.
- `python3 -m pip` always uses the same interpreter as `python3`, so the install and the run can't mismatch.
`─────────────────────────────────────────────────`

**Check which interpreter runs your script**

```sh
python3 -c "import sys; print(sys.executable)"
python3 -m pip show requests
```

If `pip show` prints "Package(s) not found", `requests` isn't installed for that interpreter.

**Fix it with a virtual environment**

Homebrew Python on macOS often refuses a global install with `externally-managed-environment`, so a venv is the safest route:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install requests
python your_script.py
```

If you run the script from an IDE, also select `.venv/bin/python` as its interpreter. Otherwise the IDE keeps using the old one and the error returns.

Next step: run the two check commands and tell me the output if the error persists. I can also inspect your project folder to see which interpreter it's using.
