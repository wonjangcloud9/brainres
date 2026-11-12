<!-- Q: Write a function that reads a CSV file and returns the average of the price column. -->

Here is a Python function that uses only the standard library and returns the mean of the `price` column.

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
            if value:  # skip blank cells
                total += float(value)
                count += 1
    if count == 0:
        raise ValueError(f"No numeric values in column '{column}'")
    return total / count
```

Example with a `products.csv` like this:

```
name,price
apple,1.50
pear,2.50
fig,
```

`average_price("products.csv")` returns `2.0`, because the blank fig price is skipped.

- **Blank cells:** they are skipped, not counted as 0. If you want them as 0, remove the `if value:` check and use `float(value or 0)`.
- **Currency symbols or thousands separators** (`$1,200.00`) will raise `ValueError`. Strip them first with `value.replace("$", "").replace(",", "")`.
- **Large files:** the function streams row by row, so memory use stays constant.

I haven't run it. If you want, I can save it to a file with a few tests, or write a pandas version (`pd.read_csv(path)["price"].mean()`) instead.
