<!-- Q: Why am I getting this?

```
Traceback (most recent call last):
  File "app.py", line 3, in <module>
    import requests
ModuleNotFoundError: No module named 'requests'
``` -->

`requests` isn't installed in the Python interpreter that runs `app.py`. Python only finds packages installed for the interpreter running the script, so a package installed for a different Python (or a different virtual environment) won't load.

Install it with the same interpreter that runs the app:

```bash
python3 -m pip install requests
python3 app.py
```

`python3 -m pip` ties the install to `python3`, which avoids a mismatch where a bare `pip` belongs to another Python.

If it still fails, check which interpreter runs the app:

```bash
python3 -c "import sys; print(sys.executable)"
```

If you use a virtual environment, activate it first (`source .venv/bin/activate`) and install there. If the project has a `requirements.txt`, run `python3 -m pip install -r requirements.txt` to install all its dependencies at once.
