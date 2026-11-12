<!-- Q: I'm learning Python. This is supposed to add up the even numbers but it always returns 0. What's wrong?

```python
def sum_even(nums):
    total = 0
    for n in nums:
        if n % 2 == 0:
            total + n
    return total
``` -->

Line 5, `total + n`, calculates a sum but never stores it, so `total` stays 0.

Change it to:

```python
total += n
```

`total + n` is a valid expression, so Python doesn't raise an error. It computes the result and throws it away. `total += n` is shorthand for `total = total + n`, which saves the result back into `total`.

With the fix, `sum_even([1, 2, 3, 4])` returns `6`.

Next, try the fixed version on a list with no even numbers, like `[1, 3]`. It should return 0 because there is nothing to add.
