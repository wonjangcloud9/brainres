<!-- Q: Write a function that reads a CSV file and returns the average of the price column. -->

This Python function uses only the standard library and skips blank price cells:

```python
import csv

def average_price(path: str, column: str = "price") -> float:
    total = 0.0
    count = 0
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if column not in (reader.fieldnames or []):
            raise KeyError(f"Column '{column}' not found in {path}")
        for row in reader:
            value = row[column].strip()
            if value:
                total += float(value)
                count += 1
    if count == 0:
        raise ValueError(f"No numeric values in column '{column}'")
    return total / count
```

Example with a `products.csv` like this:

```csv
name,price
apple,1.50
pear,2.50
plum,
```

`average_price("products.csv")` returns `2.0`, because the blank plum row is skipped.

It raises `ValueError` on non-numeric text such as `"$1.50"` rather than silently skipping it. If your data has currency symbols or thousands separators, strip them before `float()`, for example `value.replace("$", "").replace(",", "")`.

Tell me if you want a different language, or pandas (`pd.read_csv(path)["price"].mean()`) for larger files.
