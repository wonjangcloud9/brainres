<!-- Q: My Python script crashes with KeyError: 'email' when I read user records. What's wrong? -->

At least one record is missing the `'email'` key, and `record['email']` raises `KeyError` instead of returning a default. I haven't seen your script yet, so this is the usual cause, not a confirmed diagnosis.

**Common reasons the key is missing**
- Some records genuinely have no email (optional field, incomplete data).
- The key is spelled differently, such as `Email`, `e-mail`, or `email_address`.
- With CSV, the header has a BOM or trailing space, so the key is actually `'\ufeffemail'` or `'email '`.
- A nested structure: the email sits under something like `record['contact']['email']`.

**Find the bad record**
```python
for i, rec in enumerate(records):
    if 'email' not in rec:
        print(i, rec)
        break
```

**Fix it**
```python
email = rec.get('email')           # None if missing
email = rec.get('email', '')       # or a default
if email: ...                      # or skip records without one
```

Use `.get()` only if a missing email is valid. If every record should have one, a missing key is a data bug, so fix the source instead of hiding it.

Paste the traceback and the few lines that read the records, or tell me the script's filename and I'll look at it directly.
