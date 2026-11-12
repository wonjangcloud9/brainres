<!-- Q: How do I set up SSH keys for GitHub? -->

Here's how to set up an SSH key for GitHub on macOS.

**1. Check for existing keys**

```bash
ls -al ~/.ssh
```

If you see `id_ed25519.pub` or `id_rsa.pub`, you already have a key. You can reuse it or create a new one.

**2. Generate a new key**

```bash
ssh-keygen -t ed25519 -C "your_github_email@example.com"
```

- Press Enter to accept the default path (`~/.ssh/id_ed25519`).
- Set a passphrase when prompted. It's optional but recommended.

**3. Start the ssh-agent and add your key**

```bash
eval "$(ssh-agent -s)"
```

Create or edit `~/.ssh/config` so macOS loads the key automatically and stores the passphrase in the Keychain:

```
Host github.com
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ed25519
```

Then add the key:

```bash
ssh-add --apple-use-keychain ~/.ssh/id_ed25519
```

On older macOS versions, use `ssh-add -K` instead.

**4. Copy the public key**

```bash
pbcopy < ~/.ssh/id_ed25519.pub
```

**5. Add the key to GitHub**

1. Go to **GitHub → Settings → SSH and GPG keys**.
2. Click **New SSH key**.
3. Give it a title, paste the key, and click **Add SSH key**.

**6. Test the connection**

```bash
ssh -T git@github.com
```

You should see: `Hi username! You've successfully authenticated...`

**7. Use SSH remotes**

For a new clone:

```bash
git clone git@github.com:username/repo.git
```

For an existing repo that uses HTTPS:

```bash
git remote set-url origin git@github.com:username/repo.git
```

**Troubleshooting**

- **"Permission denied (publickey)"**: Confirm the key is loaded with `ssh-add -l` and that the public key on GitHub matches `~/.ssh/id_ed25519.pub`.
- **Permissions errors**: Run `chmod 700 ~/.ssh` and `chmod 600 ~/.ssh/id_ed25519`.
