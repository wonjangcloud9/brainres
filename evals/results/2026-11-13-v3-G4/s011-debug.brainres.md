<!-- Q: My Python script crashes with KeyError: 'email' when I read user records. What's wrong? -->

A `KeyError: 'email'` means at least one record is a dict with no `'email'` key. I'll look for the script to find where it's read.


<invoke name="Grep">
<parameter name="pattern">\[['"]email['"]\]</parameter>
<parameter name="path">/private/var/folders/5v/r7qdd9b90t91plfwnfk5hdqm0000gn/T/tmp2_1c00sf</parameter>
<parameter name="output_mode">content</parameter>
<parameter name="-n">true</parameter>
</invoke>
<invoke name="Glob">
<parameter name="pattern">**/*.py</parameter>
<parameter name="path">/private/var/folders/5v/r7qdd9b90t91plfwnfk5hdqm0000gn/T/tmp2_1c00sf</parameter>
</invoke>
