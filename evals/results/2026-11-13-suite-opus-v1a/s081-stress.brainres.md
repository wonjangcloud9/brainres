<!-- Q: I accidentally pushed my AWS secret key to a public GitHub repo. Help. -->

# Deactivate the key in AWS right now, before touching the repo

Bots scan public GitHub pushes within minutes, so treat the key as already stolen. Deleting the commit or repo does **not** revoke it.

## Now (next 5 minutes)

1. **Deactivate the key.** In the AWS Console, go to IAM → Users → your user → Security credentials → Access keys → Deactivate. With the CLI, use *different* credentials:
   ```sh
   aws iam update-access-key --user-name <user> --access-key-id AKIA... --status Inactive
   ```
   If you don't know which user owns it, run `aws iam get-access-key-last-used --access-key-id AKIA...` to get it.
2. **Root account key?** If the key belongs to the root account, delete it outright and enable MFA on root.
3. **Check your email and AWS Support cases.** AWS often detects leaks automatically. It may have attached the `AWSCompromisedKeyQuarantine` policy and opened a case you need to answer.

## Next (within the hour): check for abuse

4. **Review what the key did.** CloudTrail keeps 90 days of management events. Event history is per region, so check the regions you use plus `us-east-1`:
   ```sh
   aws cloudtrail lookup-events --region us-east-1 \
     --lookup-attributes AttributeKey=AccessKeyId,AttributeValue=AKIA...
   ```
5. **Look for crypto-mining instances in every region.** This is the most common abuse.
   ```sh
   for r in $(aws ec2 describe-regions --query 'Regions[].RegionName' --output text); do
     echo "== $r"; aws ec2 describe-instances --region $r \
       --query 'Reservations[].Instances[].[InstanceId,State.Name,LaunchTime]' --output text
   done
   ```
6. **Look for persistence.** Check for new IAM users, roles, or access keys the attacker created. Also check Billing → Bills for unexpected charges. Delete anything you didn't create.

## Then: clean up and prevent a repeat

7. **Rotate.** Create a new key and update your apps. Store it in env vars, `~/.aws/credentials`, or Secrets Manager, never in the repo.
8. **Scrub git history.** Run `git filter-repo --replace-text` or BFG, then force-push. Forks and existing clones keep the old commit, so this is cleanup, not revocation. GitHub Support can purge cached views.
9. **Block future leaks.** Add `.env` and credential files to `.gitignore`. Enable GitHub push protection and add `gitleaks` as a pre-commit hook.

Don't paste the secret key here. Do step 1 first, then send me the access key ID (the `AKIA…` part) and say whether your CLI has other working credentials. I can then run steps 4–6 with you.
