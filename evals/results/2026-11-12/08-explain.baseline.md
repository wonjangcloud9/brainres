<!-- Q: Explain how HTTPS keeps my password safe. -->

HTTPS wraps your HTTP traffic in TLS (Transport Layer Security), which protects your password in three ways: **confidentiality**, **integrity**, and **authentication**.

## 1. Setting up a secure channel (the TLS handshake)

When your browser connects to a site:

1. **Hello:** Your browser tells the server which TLS versions and cipher suites it supports. The server picks one.
2. **Certificate:** The server sends its certificate, which contains its public key and is signed by a Certificate Authority (CA) your device already trusts.
3. **Key exchange:** Both sides use an ephemeral Diffie-Hellman exchange (ECDHE in modern TLS) to independently compute the same shared secret. That secret is never sent over the network.
4. **Session keys:** Both sides derive symmetric encryption keys from that secret, and the handshake is confirmed as unmodified.

## 2. Confidentiality (encryption)

Once the keys exist, everything, including the URL path, headers, cookies, and your submitted password, is encrypted with a fast symmetric cipher (e.g. AES-GCM or ChaCha20-Poly1305). Anyone on the path (Wi-Fi snoopers, your ISP, routers) sees only ciphertext, plus the server's hostname and roughly how much data moves.

Because the key exchange is ephemeral, you also get **forward secrecy**: even if the server's private key leaks later, recorded past traffic can't be decrypted.

## 3. Integrity

The ciphers used are AEAD modes, so each record carries an authentication tag. If an attacker alters or injects data in transit, decryption fails and the connection is dropped. They can't silently change what you send.

## 4. Authentication (are you talking to the real site?)

Encryption alone isn't enough, since you could be encrypting traffic straight to an attacker. The certificate check covers this:

- The certificate must be signed by a trusted CA.
- It must match the domain you typed.
- It must be unexpired and not revoked.

A man-in-the-middle can't present a valid certificate for `yourbank.com` without that site's private key or a compromised CA, so your browser shows a warning instead.

## What HTTPS does *not* protect against

- **Phishing:** If you're on `yourbank-login.evil.com` with a valid certificate, your password is safely encrypted *to the attacker*.
- **Malware or keyloggers** on your device.
- **A compromised or careless server:** The server still receives your plaintext password after decryption. Good sites hash it (bcrypt, scrypt, Argon2), but that's the site's responsibility, not HTTPS's.
- **Metadata:** The domain name (via SNI/DNS, unless using ECH/DoH) and traffic timing are partly visible.
- **Weak passwords or reuse:** HTTPS doesn't help if the password is leaked elsewhere.

## Practical takeaways

- Check that the URL is the correct domain, not just that there's a padlock.
- Never click through certificate warnings.
- Use a password manager (it also refuses to autofill on look-alike domains) and enable MFA.
