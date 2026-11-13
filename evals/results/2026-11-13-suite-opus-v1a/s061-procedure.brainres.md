<!-- Q: How do I set up SSH keys for GitHub? -->

Generate an Ed25519 key, load it into the macOS keychain, then paste the public half into GitHub.

1. **Generate the key.** Press Enter to accept the default path, and set a passphrase.
   ```zsh
   ssh-keygen -t ed25519 -C "your_email@example.com"
   ```
   Run `ls ~/.ssh/id_*.pub` first. If a key already exists, you can reuse it and skip this step.

2. **Add it to the agent and keychain.** Create or edit `~/.ssh/config` with:
   ```
   Host github.com
     AddKeysToAgent yes
     UseKeychain yes
     IdentityFile ~/.ssh/id_ed25519
   ```
   Then run:
   ```zsh
   eval "$(ssh-agent -s)"
   ssh-add --apple-use-keychain ~/.ssh/id_ed25519
   ```

3. **Add the public key to GitHub.** Copy it with:
   ```zsh
   pbcopy < ~/.ssh/id_ed25519.pub
   ```
   In GitHub, go to **Settings → SSH and GPG keys → New SSH key**. Paste the key and save. Only paste the file ending in **`.pub`**. Never share `~/.ssh/id_ed25519`, because that file is your private key.

4. **Test the connection.**
   ```zsh
   ssh -T git@github.com
   ```
   On the first connection, type `yes` to trust the host. Success looks like: `Hi <username>! You've successfully authenticated, but GitHub does not provide shell access.`

Next, point existing repos at SSH instead of HTTPS:
```zsh
git remote set-url origin git@github.com:OWNER/REPO.git
```
