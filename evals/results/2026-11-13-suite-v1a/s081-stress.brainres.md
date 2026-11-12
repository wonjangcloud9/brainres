<!-- Q: I accidentally pushed my AWS secret key to a public GitHub repo. Help. -->

**Revoke the key now, before touching git.** Bots scrape GitHub within minutes, so treat the key as already stolen. Deleting the commit or repo does not undo that.

1. **Deactivate the key.** In the IAM console, or with the CLI:
   ```
   aws iam update-access-key --user-name <USER> --access-key-id <AKIA...> --status Inactive
   ```
2. **Check for abuse.** Look at CloudTrail for activity from that key:
   ```
   aws cloudtrail lookup-events --lookup-attributes AttributeKey=AccessKeyId,AttributeValue=<AKIA...>
   ```
   Also check the Billing console and every region for EC2 instances, new IAM users or roles, and new access keys. Attackers often start crypto miners and create backdoor users.
3. **Replace the key.** Create a new one, update your apps, then delete the old one:
   ```
   aws iam create-access-key --user-name <USER>
   aws iam delete-access-key --user-name <USER> --access-key-id <AKIA...>
   ```
4. **Clean up the repo.** Only do this after steps 1-3. Remove the secret from history with `git filter-repo` or BFG, then force-push. This is hygiene only, because forks and caches may still hold the key. Afterward, use environment variables or a secrets manager, and enable GitHub push protection.

AWS may also have emailed you or attached an `AWSCompromisedKeyQuarantine` policy to the user. If it did, you still need to do steps 1-3 yourself, and you can ask AWS Support to review any charges you did not cause.

Don't paste the key here. I can run the commands above or set up history cleanup for you, so tell me the IAM user name and whether the repo is local. The working directory here isn't a git repo.
