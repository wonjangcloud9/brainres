<!-- Q: How do I set up SSH keys for GitHub? -->

Here's the setup on macOS (zsh):

**1. Check for existing keys**
```sh
ls -al ~/.ssh
```
If you see `id_ed25519` and `id_ed25519.pub`, you can reuse them and skip to step 3.

**2. Generate a new key**
```sh
ssh-keygen -t ed25519 -C "your_email@example.com"
```
Press Enter to accept the default path, and set a passphrase when prompted. The email is just a label; you can use your GitHub noreply address if you prefer to keep your real one private.

**3. Add the key to the ssh-agent (with macOS Keychain)**
```sh
eval "$(ssh-agent -s)"
```
Then add this to `~/.ssh/config` (create the file if needed):
```
Host github.com
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ed25519
```
Load the key:
```sh
ssh-add --apple-use-keychain ~/.ssh/id_ed25519
```

**4. Add the public key to GitHub**
```sh
pbcopy < ~/.ssh/id_ed25519.pub
```
Then go to GitHub → Settings → SSH and GPG keys → New SSH key, give it a title, leave type as "Authentication Key", paste, and save.

Or with the GitHub CLI:
```sh
gh ssh-key add ~/.ssh/id_ed25519.pub --title "My Mac"
```

**5. Test the connection**
```sh
ssh -T git@github.com
```
The first time, confirm the host fingerprint (compare it against GitHub's published fingerprints). You should see: `Hi <username>! You've successfully authenticated, but GitHub does not provide shell access.`

**6. Use SSH remotes**
For existing repos switch from HTTPS:
```sh
git remote set-url origin git@github.com:OWNER/REPO.git
```
New clones use `git clone git@github.com:OWNER/REPO.git`.

**Troubleshooting**
- `Permission denied (publickey)`: run `ssh -vT git@github.com` and check that your key is offered; confirm it's loaded with `ssh-add -l`.
- Never share the private key (`id_ed25519`, no `.pub`); only the `.pub` file goes to GitHub.

I can run the checks or generate the key for you here if you'd like.
