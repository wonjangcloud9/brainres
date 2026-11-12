<!-- Q: I'm learning Python. This is supposed to add up the even numbers but it always returns 0. What's wrong?

```python
def sum_even(nums):
    total = 0
    for n in nums:
        if n % 2 == 0:
            total + n
    return total
``` -->

`total + n` computes a sum but throws it away, so `total` stays 0. You need `total += n` (or `total = total + n`).

```python
def sum_even(nums):
    total = 0
    for n in nums:
        if n % 2 == 0:
            total += n
    return total
```

Python evaluates `total + n` as an expression, like `5 + 3`, but nothing stores the result. Assignment (`=` or `+=`) is what updates a variable. For `[1, 2, 3, 4]`, the fixed version returns `6`.

Quick check: what would `sum_even([1, 3, 5])` return, and why?
