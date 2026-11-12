<!-- Q: How do I set up SSH keys for GitHub? -->

Generate an ed25519 key, add it to your ssh-agent, and paste the public key into GitHub under Settings → SSH and GPG keys.

**1. Generate the key**

```sh
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Press Enter to accept the default path (`~/.ssh/id_ed25519`). Set a passphrase when prompted. The comment (`-C`) is only a label, so use any identifier you like.

**2. Add it to the agent (macOS)**

Add this to `~/.ssh/config` (create the file if missing):

```
Host github.com
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ed25519
```

Then load the key:

```sh
ssh-add --apple-use-keychain ~/.ssh/id_ed25519
```

This stores the passphrase in the macOS Keychain, so you won't retype it.

**3. Add the public key to GitHub**

```sh
pbcopy < ~/.ssh/id_ed25519.pub
```

Then go to github.com → Settings → SSH and GPG keys → New SSH key. Paste it, give it a title, and choose "Authentication Key".

Copy only the `.pub` file. **Never share the file without `.pub`**, because that is your private key.

**4. Test it**

```sh
ssh -T git@github.com
```

The first time, confirm the host fingerprint matches GitHub's published one, then type `yes`. Success looks like: `Hi <username>! You've successfully authenticated...`

**5. Use SSH URLs**

For existing repos that were cloned over HTTPS:

```sh
git remote set-url origin git@github.com:OWNER/REPO.git
```

New clones should use the `git@github.com:OWNER/REPO.git` form.

If the test fails with `Permission denied (publickey)`, run `ssh -vT git@github.com` and check that it offers your key. Usually the key isn't loaded in the agent (`ssh-add -l` lists loaded keys).
