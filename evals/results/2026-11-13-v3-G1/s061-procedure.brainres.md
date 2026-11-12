<!-- Q: How do I set up SSH keys for GitHub? -->

Here is the setup on macOS (zsh).

1. **Generate a key.** Use a passphrase when prompted, and accept the default path.
   ```sh
   ssh-keygen -t ed25519 -C "your_email@example.com"
   ```
   The `-C` value is only a label, so any string works.

2. **Add it to ssh-agent and the macOS Keychain.** Put this in `~/.ssh/config`:
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

3. **Copy the public key.**
   ```sh
   pbcopy < ~/.ssh/id_ed25519.pub
   ```
   Copy only the `.pub` file. **Never share the file without `.pub`**, because it is your private key.

4. **Add it on GitHub.** Go to Settings → SSH and GPG keys → New SSH key. Give it a title, keep the type as "Authentication Key", paste the key, and save.

5. **Test the connection.**
   ```sh
   ssh -T git@github.com
   ```
   The first time, confirm the host fingerprint prompt. Success looks like `Hi <username>! You've successfully authenticated`.

6. **Use SSH URLs for repos.** For an existing clone that uses HTTPS:
   ```sh
   git remote set-url origin git@github.com:OWNER/REPO.git
   ```

If step 5 fails with `Permission denied (publickey)`, run `ssh-add -l` to check the key is loaded, then `ssh -vT git@github.com` to see which key is offered.

Want me to check your existing `~/.ssh` setup or run these steps for you?
