<!-- Q: Explain how HTTPS keeps my password safe. -->

HTTPS wraps your traffic in TLS, so your password is encrypted in transit and only the server you intended can read it.

**How it works:**

1. **Authentication:** The server presents a certificate signed by a trusted certificate authority. Your browser verifies it matches the domain, so you know you're talking to the real site, not an impostor.
2. **Key exchange:** Your browser and the server use an ephemeral Diffie-Hellman exchange to agree on a shared secret over the open network. An eavesdropper who sees the whole exchange still can't derive the secret.
3. **Encryption:** Both sides derive session keys from that secret and encrypt everything with an authenticated cipher (e.g., AES-GCM or ChaCha20-Poly1305). Your password travels as ciphertext.
4. **Integrity:** The authenticated cipher also detects tampering, so someone on the network can't alter requests or responses undetected.
5. **Forward secrecy:** Because the keys are ephemeral, stealing the server's private key later doesn't let anyone decrypt recorded past sessions.

**What it doesn't protect against:**

- Phishing: a look-alike domain with a valid certificate gets your password just fine.
- Malware or a malicious browser extension on your device.
- A compromised or careless server (e.g., one that logs or stores passwords in plaintext, or stores them poorly hashed).
- Weak or reused passwords.

So HTTPS protects the password on the wire; a password manager and 2FA cover most of the rest.
