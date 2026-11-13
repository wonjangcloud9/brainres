<!-- Q: My Python script crashes with KeyError: 'email' when I read user records. What's wrong? -->

The cause is almost certainly that some record lacks an `"email"` key, so `record["email"]` raises. I'll look for the script to confirm.


<invoke name="Grep">
<parameter name="pattern">\[['"]email['"]\]</parameter>
<parameter name="glob">*.py</parameter>
<parameter name="output_mode">content</parameter>
<parameter name="-n">true</parameter>
</invoke>
<invoke name="Glob">
<parameter name="pattern">**/*.py</parameter>
</invoke>
