<!-- Q: My Python script says ModuleNotFoundError: No module named 'requests'. Why? -->

Python can't find `requests` because the interpreter running your script doesn't have it installed. The usual cause is that `pip install requests` went into a different Python than the one running the script. On macOS this is common because `pip` and `python3` often point to different installs (Homebrew, system, a venv, pyenv).

Install it with the same interpreter that runs the script:

```zsh
python3 -m pip install requests
python3 your_script.py
```

`python3 -m pip` guarantees pip and Python match. If the install fails with `externally-managed-environment` (common with Homebrew Python), use a virtual environment:

```zsh
python3 -m venv .venv
source .venv/bin/activate
pip install requests
python your_script.py
```

To confirm a mismatch, compare these two outputs. If the paths differ, that's the cause.

```zsh
which python3 pip
python3 -m pip --version
```

If you run the script from an IDE (VS Code, PyCharm), also check that its selected interpreter is the one where you installed `requests`.

Run `python3 -m pip install requests` first, and if it still fails, paste the output of the `which` command above.
