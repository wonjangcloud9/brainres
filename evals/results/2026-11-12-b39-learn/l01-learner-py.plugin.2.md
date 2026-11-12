<!-- Q: I'm learning Python. This is supposed to add up the even numbers but it always returns 0. What's wrong?

```python
def sum_even(nums):
    total = 0
    for n in nums:
        if n % 2 == 0:
            total + n
    return total
``` -->

The bug is the line `total + n`: it calculates a sum but never stores it, so `total` stays 0. Change it to `total += n`:

```python
def sum_even(nums):
    total = 0
    for n in nums:
        if n % 2 == 0:
            total += n
    return total
```

`total += n` is shorthand for `total = total + n`. It assigns the result back to `total`. A bare `total + n` is a valid expression, so Python doesn't raise an error. It just discards the result.

Your even check (`n % 2 == 0`) is correct. To test the fix, run `sum_even([1, 2, 3, 4])`. It should return `6`.
