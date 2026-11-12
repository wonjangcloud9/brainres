<!-- Q: Why am I getting this?

```
Traceback (most recent call last):
  File "app.py", line 3, in <module>
    import requests
ModuleNotFoundError: No module named 'requests'
``` -->

The `requests` library isn't installed for the Python that runs `app.py`. Python only finds modules in its own environment, so a package installed elsewhere won't be visible.

Install it with the same interpreter that runs your script:

```bash
python3 -m pip install requests
```

Then confirm it works:

```bash
python3 -c "import requests; print(requests.__version__)"
```

If you use a virtual environment, activate it first. If the error persists after installing, you may have two Python installs. Run `which python3` and `python3 -m pip --version` to check that pip points to the same interpreter. I can't see your machine, so those two outputs will settle it.
