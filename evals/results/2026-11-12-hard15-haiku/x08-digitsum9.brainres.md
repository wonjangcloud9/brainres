<!-- Q: How many 4-digit numbers have digits that add up to 9? -->

**165** four-digit numbers (1000 to 9999) have digits that sum to 9.

Let the first digit be $a \ge 1$. Write $a' = a - 1 \ge 0$, so $a' + b + c + d = 8$ with all variables nonnegative. Stars and bars gives $\binom{11}{3} = 165$. Every digit is automatically at most 9, since the total is 8.

As a check, allowing leading zeros gives $\binom{12}{3} = 220$ strings. Removing the 55 with a leading zero ($b + c + d = 9$, $\binom{11}{2} = 55$) leaves 165.
