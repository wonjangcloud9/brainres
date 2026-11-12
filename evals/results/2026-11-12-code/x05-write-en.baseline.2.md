<!-- Q: Write a function that reads a CSV file and returns the average of the price column. -->

```python
import csv


def average_price(path, column="price"):
    """Return the average of the `price` column in a CSV file.

    Blank or non-numeric values are skipped. Returns None if no valid
    values are found.
    """
    total = 0.0
    count = 0
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        if column not in (reader.fieldnames or []):
            raise KeyError(f"Column '{column}' not found in {path}")
        for row in reader:
            value = (row[column] or "").strip().replace(",", "")
            try:
                total += float(value)
                count += 1
            except ValueError:
                continue
    return total / count if count else None
```

Usage:

```python
print(average_price("products.csv"))
```

Notes:
- Streams the file row by row, so it handles large files.
- `utf-8-sig` handles a BOM from Excel exports.
- Strips thousands separators (`1,200.50`) but not currency symbols; add `.replace("$", "")` if needed.
- Raises `KeyError` if there's no `price` column; the `column` argument lets you reuse it for other columns.
