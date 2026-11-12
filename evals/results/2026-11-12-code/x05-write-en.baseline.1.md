<!-- Q: Write a function that reads a CSV file and returns the average of the price column. -->

```python
import csv

def average_price(path, column="price"):
    """Return the average of the given column in a CSV file.

    Skips blank or non-numeric values. Raises ValueError if the column
    is missing or contains no valid numbers.
    """
    total = 0.0
    count = 0
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None or column not in reader.fieldnames:
            raise ValueError(f"Column '{column}' not found in {path}")
        for row in reader:
            value = (row[column] or "").strip()
            if not value:
                continue
            try:
                total += float(value.replace(",", "").lstrip("$"))
                count += 1
            except ValueError:
                continue
    if count == 0:
        raise ValueError(f"No numeric values found in column '{column}'")
    return total / count
```

Usage:

```python
print(average_price("products.csv"))
```

Notes:
- Uses `csv.DictReader`, so the column is found by header name, not position.
- Blank and non-numeric cells are skipped; also strips a leading `$` and thousands commas.
- If you'd rather use pandas: `pd.read_csv(path)["price"].mean()`.

I can save this to a file in the working directory if you'd like.
