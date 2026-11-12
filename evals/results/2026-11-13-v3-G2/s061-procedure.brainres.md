<!-- Q: How do I set up SSH keys for GitHub? -->

Generate an Ed25519 key, add it to your macOS ssh-agent, and paste the public key into GitHub under Settings → SSH and GPG keys.

1. Generate the key (use your own email as the comment):
   ```sh
   ssh-keygen -t ed25519 -C "your_email@example.com"
   ```
   Press Enter to accept the default path (`~/.ssh/id_ed25519`), and set a passphrase.

2. Start the agent and add the key to the macOS keychain:
   ```sh
   eval "$(ssh-agent -s)"
   ssh-add --apple-use-keychain ~/.ssh/id_ed25519
   ```

3. Make this persistent by adding this to `~/.ssh/config`:
   ```
   Host github.com
     AddKeysToAgent yes
     UseKeychain yes
     IdentityFile ~/.ssh/id_ed25519
   ```

4. Copy the **public** key (the `.pub` file), never the private one:
   ```sh
   pbcopy < ~/.ssh/id_ed25519.pub
   ```

5. In GitHub, go to Settings → SSH and GPG keys → New SSH key. Give it a title, keep the type as "Authentication Key", paste, and save.

6. Test the connection:
   ```sh
   ssh -T git@github.com
   ```
   The first time, confirm the host fingerprint prompt. Success looks like `Hi <username>! You've successfully authenticated...`.

7. Use SSH URLs for your repos. For an existing clone, switch the remote:
   ```sh
   git remote set-url origin git@github.com:OWNER/REPO.git
   ```

If step 6 fails with `Permission denied (publickey)`, run `ssh -vT git@github.com` and check that it offers `~/.ssh/id_ed25519`. Also confirm `ssh-add -l` lists the key.

Want me to check your existing `~/.ssh` folder for keys before you generate a new one?
