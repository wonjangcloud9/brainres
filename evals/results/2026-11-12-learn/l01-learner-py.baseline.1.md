<!-- Q: I'm learning Python. This is supposed to add up the even numbers but it always returns 0. What's wrong?

```python
def sum_even(nums):
    total = 0
    for n in nums:
        if n % 2 == 0:
            total + n
    return total
``` -->

The bug is this line:

```python
total + n
```

This calculates `total + n` but doesn't store the result anywhere, so `total` stays at 0. You need to assign it back:

```python
total = total + n
```

or the shorter form:

```python
total += n
```

Fixed version:

```python
def sum_even(nums):
    total = 0
    for n in nums:
        if n % 2 == 0:
            total += n
    return total

print(sum_even([1, 2, 3, 4, 5, 6]))  # 12
```

A good habit: an expression on its own line, like `total + n`, is valid Python but does nothing useful. If you see a line that computes something without assigning or using it, that's often a bug.
