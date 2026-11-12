<!-- Q: I'm learning Python. This is supposed to add up the even numbers but it always returns 0. What's wrong?

```python
def sum_even(nums):
    total = 0
    for n in nums:
        if n % 2 == 0:
            total + n
    return total
``` -->

Line 5 uses `total + n`, which calculates a sum but never stores it, so `total` stays 0. Change it to:

```python
total += n
```

`total + n` is an expression that produces a value and then throws it away. `total += n` is shorthand for `total = total + n`, which assigns the result back to `total`.

Fixed function:

```python
def sum_even(nums):
    total = 0
    for n in nums:
        if n % 2 == 0:
            total += n
    return total

print(sum_even([1, 2, 3, 4]))  # 6
```

Try it with your own list to confirm it returns the sum of the even numbers.
