<!-- Q: I'm learning Python. This is supposed to add up the even numbers but it always returns 0. What's wrong?

```python
def sum_even(nums):
    total = 0
    for n in nums:
        if n % 2 == 0:
            total + n
    return total
``` -->

`total + n` computes a sum but throws it away, so `total` never changes and stays 0; you need `total += n`.

Fixed code:

```python
def sum_even(nums):
    total = 0
    for n in nums:
        if n % 2 == 0:
            total += n
    return total
```

`total + n` is an expression: Python calculates the result and discards it because nothing stores it. `total += n` is shorthand for `total = total + n`, which stores the result back into `total`.

Check: `sum_even([1, 2, 3, 4])` should now return `6` (2 + 4).

Next step: run that example, then try `sum_even([])`, which should return `0`.
