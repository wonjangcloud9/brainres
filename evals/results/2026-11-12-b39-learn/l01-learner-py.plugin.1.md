<!-- Q: I'm learning Python. This is supposed to add up the even numbers but it always returns 0. What's wrong?

```python
def sum_even(nums):
    total = 0
    for n in nums:
        if n % 2 == 0:
            total + n
    return total
``` -->

The line `total + n` calculates a sum but throws the result away, so `total` stays 0. Change it to `total += n`, which means `total = total + n` and saves the result back into `total`.

```python
def sum_even(nums):
    total = 0
    for n in nums:
        if n % 2 == 0:
            total += n
    return total

print(sum_even([1, 2, 3, 4]))  # 6
```

Python doesn't complain about `total + n` because it's a valid expression. It just isn't assigned to anything. Your `if n % 2 == 0` check was correct.

Next, try `sum_even([1, 2, 3, 4])` yourself. It should print 6, because 2 + 4 = 6.
