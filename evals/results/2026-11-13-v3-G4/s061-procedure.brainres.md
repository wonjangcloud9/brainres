<!-- Q: How do I set up SSH keys for GitHub? -->

Generate an Ed25519 key, add it to the ssh-agent, and paste the public key into GitHub under Settings → SSH and GPG keys.

**1. Generate the key** (use your GitHub email as the comment):

```sh
ssh-keygen -t ed25519 -C "you@example.com"
```

Accept the default path (`~/.ssh/id_ed25519`) and set a passphrase.

**2. Add it to the agent and macOS Keychain.** Put this in `~/.ssh/config`:

```
Host github.com
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ed25519
```

Then run:

```sh
ssh-add --apple-use-keychain ~/.ssh/id_ed25519
```

**3. Copy the public key:**

```sh
pbcopy < ~/.ssh/id_ed25519.pub
```

**4. Add it on GitHub:** Settings → SSH and GPG keys → New SSH key. Choose type "Authentication Key", give it a title (e.g. "MacBook"), paste, and save.

**5. Test it:**

```sh
ssh -T git@github.com
```

The first time, confirm the host fingerprint matches GitHub's published one, then type `yes`. You should see "Hi <username>! You've successfully authenticated."

**6. Use SSH remotes.** For existing repos, switch from HTTPS:

```sh
git remote set-url origin git@github.com:OWNER/REPO.git
```

Only share the `.pub` file, never `id_ed25519` itself.

Want me to run steps 1–2 for you here? I'd check for an existing `~/.ssh/id_ed25519` first so nothing gets overwritten.
