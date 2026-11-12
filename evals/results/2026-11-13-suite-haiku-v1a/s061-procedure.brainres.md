<!-- Q: How do I set up SSH keys for GitHub? -->

Run these steps in Terminal on your Mac.

**1. Generate a key**

```bash
ssh-keygen -t ed25519 -C "your_github_email@example.com"
```

Press Enter to accept the default path (`~/.ssh/id_ed25519`). Set a passphrase when prompted.

**2. Add the key to the agent and macOS Keychain**

```bash
eval "$(ssh-agent -s)"
ssh-add --apple-use-keychain ~/.ssh/id_ed25519
```

**3. Copy the public key**

```bash
pbcopy < ~/.ssh/id_ed25519.pub
```

**4. Add it to GitHub**

Go to **Settings → SSH and GPG keys → New SSH key**, paste the key, and save.

**5. Test the connection**

```bash
ssh -T git@github.com
```

A message like `Hi username! You've successfully authenticated...` means it works.

**6. Use SSH remotes**

For an existing repo, switch the remote:

```bash
git remote set-url origin git@github.com:USERNAME/REPO.git
```

Check the result with `git remote -v`.

If `ssh-add` fails, add this to `~/.ssh/config` so macOS loads the key automatically:

```
Host github.com
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ed25519
```
