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

That computes `total + n` but throws the result away, so `total` never changes. You need to assign it back:

```python
total = total + n
```

or the shorthand:

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

An expression on its own line (like `total + n`) is valid Python, so you get no error. It just doesn't do anything useful. Whenever a result seems to be ignored, check that you're actually storing it somewhere.
