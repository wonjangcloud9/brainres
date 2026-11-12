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

Change it to `total += n` (short for `total = total + n`):

```python
def sum_even(nums):
    total = 0
    for n in nums:
        if n % 2 == 0:
            total += n
    return total
```

Now `sum_even([1, 2, 3, 4])` returns 6, because 2 + 4 are added into `total`.

Python doesn't warn about `total + n` because it's a valid expression. It just throws the result away. Try the fixed version with your own list to confirm.
