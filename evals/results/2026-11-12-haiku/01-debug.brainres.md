<!-- Q: My Python script says ModuleNotFoundError: No module named 'requests'. Why? -->

The Python running your script can't find `requests`, because it isn't installed in that interpreter. Your machine likely has several Python installs, and `requests` may be in a different one.

Check which Python runs the script and whether it has `requests`:

```bash
which python3
python3 -c "import sys; print(sys.executable)"
python3 -c "import requests; print(requests.__version__)"
```

Then install `requests` into that same interpreter:

```bash
python3 -m pip install requests
```

Using `python3 -m pip` instead of plain `pip` ensures the package goes into the interpreter you run, not a different one.

Common causes:

- **Multiple Pythons:** Installing with `pip` put `requests` into one Python, and running `python3` uses another.
- **Virtual environment:** If you activated a `venv` at some point, install inside it, or run the script with the venv's own interpreter (for example, `./venv/bin/python script.py`).
- **IDE mismatch:** VS Code or PyCharm may use a different interpreter than your terminal. Select the interpreter in the IDE settings.

If the install succeeds but the error stays, paste the output of the first three commands here and I'll find the mismatch.
