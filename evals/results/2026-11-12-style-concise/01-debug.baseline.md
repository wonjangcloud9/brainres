<!-- Q: My Python script says ModuleNotFoundError: No module named 'requests'. Why? -->

The Python interpreter running your script doesn't have `requests` installed. This usually happens because `pip` installed it into a different Python than the one running the script (common with multiple Pythons or virtual environments on macOS).

Fix: install it using the same interpreter that runs the script:

```
python3 -m pip install requests
```

To check which interpreter is in use, run `which python3` (or `python3 -c "import sys; print(sys.executable)"`). If you use a venv, activate it first (`source .venv/bin/activate`) and then install.
