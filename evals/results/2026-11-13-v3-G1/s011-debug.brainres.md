<!-- Q: My Python script crashes with KeyError: 'email' when I read user records. What's wrong? -->

I'll check the working directory for the script first.


<invoke name="Grep">
<parameter name="pattern">\[['"]email['"]\]</parameter>
<parameter name="glob">*.py</parameter>
<parameter name="output_mode">content</parameter>
<parameter name="-n">true</parameter>
</invoke>
