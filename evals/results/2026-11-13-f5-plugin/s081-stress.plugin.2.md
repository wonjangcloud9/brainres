<!-- Q: I accidentally pushed my AWS secret key to a public GitHub repo. Help. -->

**Deactivate the key now:** AWS Console → IAM → Users → your user → Security credentials → the leaked access key → **Actions → Deactivate**. Don't start by deleting the repo or rewriting git history, because bots scrape GitHub within minutes and the key is already compromised.

Then, in order:

1. **Create a new access key** and update your apps with it. Once nothing uses the old key, delete it.
2. **Check for abuse.** Open CloudTrail → Event history and look for activity from the leaked key ID that wasn't you. Also check every region for unfamiliar EC2 instances, Lambda functions, new IAM users or roles, and unexpected billing in Cost Explorer. Attackers often start crypto-mining instances.
3. **Look for AWS's notice.** AWS often emails about exposed keys and may have applied the `AWSCompromisedKeyQuarantine` policy. If you see it, it doesn't replace rotating the key.
4. **Remove the secret from the repo.** Use `git filter-repo` or BFG to purge it from history, then force-push. Scrubbing history does nothing for the leaked key itself. Forks, clones, and scrapers may already have it, so step 1 is what protects you.
5. **Prevent a repeat.** Add a `.gitignore` entry for your `.env` or credentials file. Turn on GitHub secret scanning and push protection in the repo's Security settings. Use IAM roles or AWS SSO instead of long-lived keys where you can.

If you find unauthorized activity, contact AWS Support. They often waive charges from a compromised key.

I can help with the CloudTrail check or the history cleanup. Tell me which one, and whether the repo is on this machine.
