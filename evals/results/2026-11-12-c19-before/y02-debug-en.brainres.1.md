<!-- Q: Why am I getting this?

```
Traceback (most recent call last):
  File "app.py", line 3, in <module>
    import requests
ModuleNotFoundError: No module named 'requests'
``` -->

Because the `requests` library is not installed in the Python environment that runs `app.py`. Python can only import packages that exist in its active environment, and `requests` is a third-party package, so it must be installed first.

Install it with the same Python that runs your script:

```bash
python3 -m pip install requests
```

Using `python3 -m pip` ties the install to that interpreter, which avoids the common case where `pip` installs into a different Python.

If it still fails, check which interpreter runs the script with `which python3`, and check for a virtual environment, since one may be active or missing. If you have a `requirements.txt`, run `python3 -m pip install -r requirements.txt` to install everything the project needs at once.
