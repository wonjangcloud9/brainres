<!-- Q: How do I set up SSH keys for GitHub? -->

Generate an ed25519 key, add it to the ssh-agent, then paste the public key into GitHub under Settings → SSH and GPG keys.

**1. Generate the key** (use your GitHub email as the comment, and accept the default path):

```sh
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Set a passphrase when prompted. It protects the key if your laptop is stolen.

**2. Add it to the agent and macOS Keychain** (so you type the passphrase once):

```sh
eval "$(ssh-agent -s)"
ssh-add --apple-use-keychain ~/.ssh/id_ed25519
```

Then make this persistent in `~/.ssh/config`:

```
Host github.com
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ed25519
```

**3. Copy the public key:**

```sh
pbcopy < ~/.ssh/id_ed25519.pub
```

**4. Add it on GitHub:** go to Settings → SSH and GPG keys → New SSH key, give it a title (e.g. "MacBook"), keep type "Authentication Key", paste, and save.

**5. Test:**

```sh
ssh -T git@github.com
```

The first time, confirm the host fingerprint matches GitHub's published one, then type `yes`. You should see `Hi <username>! You've successfully authenticated...`.

**6. Use SSH remotes.** Existing HTTPS repos need switching:

```sh
git remote set-url origin git@github.com:OWNER/REPO.git
```

If step 5 fails with `Permission denied (publickey)`, run `ssh -vT git@github.com` and check that it offers your `id_ed25519` key.

Want me to run any of these steps for you? I'd check first whether `~/.ssh/id_ed25519` already exists so I don't overwrite it.
