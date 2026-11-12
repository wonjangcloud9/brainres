<!-- Q: My Python script says ModuleNotFoundError: No module named 'requests'. Why? -->

The Python interpreter running your script doesn't have `requests` installed, usually because you installed it into a different Python than the one running the script.

To fix it:

1. Install it with the same interpreter that runs the script: `python3 -m pip install requests`. Use the exact command you run the script with (for example `python` or `python3.12`) in place of `python3`.
2. Check which interpreter is in use: `python3 -c "import sys; print(sys.executable)"`. If it points to a different venv or system Python than your `pip` does, that mismatch is the cause. `pip --version` shows which Python your `pip` belongs to.
3. If you use a virtual environment, activate it first (`source .venv/bin/activate`), then install.

On macOS, a bare `pip install requests` often targets a different Python than `python3`. That's why `python3 -m pip` is safer.

If it still fails after step 1, tell me the output of the step 2 command and the command you use to run the script. I can then see which interpreter is mismatched.
