<!-- Q: My Python script says ModuleNotFoundError: No module named 'requests'. Why? -->

The Python interpreter running your script doesn't have `requests` installed, usually because you installed it into a different Python than the one running the script (another version, or a virtualenv that isn't active).

Check and fix:

```sh
python3 -c "import sys; print(sys.executable)"   # which Python runs
python3 -m pip install requests                   # install into that same Python
```

Using `python3 -m pip` instead of bare `pip` guarantees the package lands in the interpreter you just checked. If you use a virtualenv, activate it first (`source .venv/bin/activate`) and run both commands again.

If it still fails, run `python3 -m pip show requests` and send me the output along with how you launch the script (terminal, IDE, or `python` vs `python3`).
