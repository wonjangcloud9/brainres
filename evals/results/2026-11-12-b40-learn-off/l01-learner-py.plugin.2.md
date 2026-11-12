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

`total + n` produces a value and then discards it, like writing `5 + 3` on its own line. `total += n` is shorthand for `total = total + n`, which assigns the result back to `total`.

With the fix, `sum_even([1, 2, 3, 4])` returns 6 (2 + 4).

Next step: make that one-character-ish change and rerun your test.
