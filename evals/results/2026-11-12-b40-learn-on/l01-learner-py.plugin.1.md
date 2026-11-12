<!-- Q: I'm learning Python. This is supposed to add up the even numbers but it always returns 0. What's wrong?

```python
def sum_even(nums):
    total = 0
    for n in nums:
        if n % 2 == 0:
            total + n
    return total
``` -->

The line `total + n` adds the two numbers but throws the result away, so `total` stays 0. Change it to:

```python
total += n
```

`total += n` is short for `total = total + n`, which stores the sum back into `total`. Your loop and `% 2 == 0` check are already correct.

With `nums = [1, 2, 3, 4]`, the fixed function returns 6, because 2 + 4 = 6.

Before you run it, what do you think `sum_even([1, 3, 5])` returns, and why?
