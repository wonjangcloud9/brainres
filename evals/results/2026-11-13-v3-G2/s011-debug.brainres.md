<!-- Q: My Python script crashes with KeyError: 'email' when I read user records. What's wrong? -->

Some record you read has no `'email'` key, and your code indexes it directly (`record['email']`), which raises `KeyError` instead of returning a default. I haven't seen your script yet, so I'll search the working directory for it.


<invoke name="Grep">
<parameter name="pattern">\[['"]email['"]\]</parameter>
<parameter name="path">/private/var/folders/5v/r7qdd9b90t91plfwnfk5hdqm0000gn/T/tmpk48rspc4</parameter>
<parameter name="output_mode">content</parameter>
<parameter name="-n">true</parameter>
</invoke>
<invoke name="Glob">
<parameter name="pattern">**/*.py</parameter>
<parameter name="path">/private/var/folders/5v/r7qdd9b90t91plfwnfk5hdqm0000gn/T/tmpk48rspc4</parameter>
</invoke>
