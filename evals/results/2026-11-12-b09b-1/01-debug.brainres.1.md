<!-- Q: My Python script says ModuleNotFoundError: No module named 'requests'. Why? -->

Because the Python interpreter running your script doesn't have `requests` installed, which is almost always a mismatch between the `pip` you installed it with and the `python` you run.

On macOS this is common: `pip` may point to one Python (Homebrew, system, or a venv) while `python3` points to another.

**Fix, in order:**

1. Check which interpreter runs your script: `python3 -c "import sys; print(sys.executable)"`
2. Install into that exact interpreter: `python3 -m pip install requests`
3. Verify: `python3 -c "import requests; print(requests.__version__)"`

Using `python3 -m pip` instead of bare `pip` guarantees the install goes where the script looks.

If step 2 fails with `externally-managed-environment` (~80% likely on Homebrew Python), create a virtual environment instead:

```
python3 -m venv .venv
source .venv/bin/activate
pip install requests
python script.py
```

If you run the script from an IDE, also check that its selected interpreter matches the one in step 1.

Run step 1 and tell me the path it prints if the error persists.
