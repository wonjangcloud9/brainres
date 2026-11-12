<!-- Q: My Python script crashes with KeyError: 'email' when I read user records. What's wrong? -->

At least one record has no `'email'` key, so `record['email']` raises `KeyError`. Your script is fine on the records that have it.

Common causes:
- **Missing field:** some users have no email, which is common in JSON or API data.
- **Different key name:** `Email`, `E-mail`, `email ` (trailing space), or `user_email`.
- **CSV with a BOM:** Excel-exported files can make the first header `'\ufeffemail'`. Open the file with `encoding="utf-8-sig"`.
- **Nested data:** the value is at `record['contact']['email']`.

To find the bad record:

```python
for i, record in enumerate(records):
    if 'email' not in record:
        print(i, sorted(record.keys()))
        break
```

If the field is legitimately optional, read it safely:

```python
email = record.get('email')          # None if missing
if email:
    send_to(email)
```

If it should always exist, keep `record['email']` and let it fail loudly, but log the offending record first so you can see what the data looks like.

If this doesn't match what you see, paste the full traceback and the code that reads the records. I can also look at the script directly if you tell me the file name.
