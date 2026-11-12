<!-- Q: In JavaScript, what does [10, 1, 2].sort() return? -->

[1, 10, 2]

`sort()` with no comparator converts each element to a string and sorts by UTF-16 code units. "1" < "10" < "2", so the numbers come out as `[1, 10, 2]`, not numerically sorted.

To sort numerically, pass a comparator: `[10, 1, 2].sort((a, b) => a - b)` returns `[1, 2, 10]`.

Note that `sort()` mutates the array in place and returns the same array reference.
