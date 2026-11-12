<!-- Q: Why am I getting this?

```
Traceback (most recent call last):
  File "app.py", line 3, in <module>
    import requests
ModuleNotFoundError: No module named 'requests'
``` -->

The `requests` package isn't installed for the Python that runs `app.py`. Python only finds modules in its own environment, so a package installed for a different Python (or a different virtualenv) won't count.

Install it with the same interpreter that runs your script:

```bash
python3 -m pip install requests
```

Running `pip` through `python3 -m` ensures the package goes into the interpreter you're actually using. Then confirm the import works:

```bash
python3 -c "import requests; print(requests.__version__)"
```

If you use a virtual environment, activate it first. If the error still appears, run `which python3` and make sure it points to the environment where you installed the package. For projects that depend on `requests`, add it to a `requirements.txt` so others can install it too.
