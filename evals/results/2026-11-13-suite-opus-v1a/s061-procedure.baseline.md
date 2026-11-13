<!-- Q: How do I set up SSH keys for GitHub? -->

# Setting up SSH keys for GitHub on macOS

### 1. Check for existing keys

```bash
ls -al ~/.ssh
```

If you already see `id_ed25519` and `id_ed25519.pub`, you can skip to step 3 and use that key.

### 2. Generate a new key

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

- Press Enter to accept the default location (`~/.ssh/id_ed25519`).
- Enter a passphrase. This is recommended, and macOS Keychain will remember it for you.

The `-C` value is just a label. Using your GitHub email is common.

### 3. Add the key to the SSH agent and Keychain

Start the agent:

```bash
eval "$(ssh-agent -s)"
```

Create or edit `~/.ssh/config` so the key loads automatically:

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

### 4. Add the public key to GitHub

Copy the **public** key (the one ending in `.pub`) to your clipboard:

```bash
pbcopy < ~/.ssh/id_ed25519.pub
```

On GitHub, go to **Settings → SSH and GPG keys → New SSH key**, paste it, give it a title (e.g. "MacBook"), and save.

If you use the GitHub CLI, this does the same thing: `gh ssh-key add ~/.ssh/id_ed25519.pub --title "MacBook"`

### 5. Test the connection

```bash
ssh -T git@github.com
```

The first time, type `yes` to trust GitHub's host fingerprint. Success looks like:

```
Hi <username>! You've successfully authenticated, but GitHub does not provide shell access.
```

### 6. Use SSH URLs for your repos

Clone with `git@github.com:user/repo.git` instead of `https://...`. For an existing repo that uses HTTPS:

```bash
git remote set-url origin git@github.com:user/repo.git
```

---

**Never share the private key** (`id_ed25519`, without `.pub`). Only the `.pub` file goes to GitHub.

I can run the check and generation steps for you if you'd like. You'd still need to type the passphrase and paste the key into GitHub yourself.
