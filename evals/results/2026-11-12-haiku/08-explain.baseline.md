<!-- Q: Explain how HTTPS keeps my password safe. -->

HTTPS protects your password by encrypting the connection between your browser and the website's server. Here's how the pieces work together:

**1. The handshake sets up a secure channel**
When you connect, your browser and the server run a TLS handshake:
- The server presents a **certificate** signed by a trusted Certificate Authority (CA). Your browser checks that the certificate matches the domain you typed and that a trusted CA vouched for it. This stops someone from impersonating the site.
- Browser and server agree on a **shared secret key** using asymmetric cryptography (e.g., ECDHE). The key is never sent over the network, so an eavesdropper who sees the handshake can't reconstruct it.

**2. Everything is encrypted with that key**
Once the handshake finishes, all data, including your password, is encrypted with symmetric encryption (e.g., AES-GCM or ChaCha20-Poly1305). Someone watching the traffic on your Wi-Fi, your ISP, or a router along the path sees only ciphertext, not the password itself.

**3. Tampering is detected**
Each message includes an authentication tag. If anyone modifies a packet in transit, the check fails and the connection is dropped. This prevents attackers from altering or replaying your login request undetected.

**4. Forward secrecy**
Because the key exchange uses ephemeral keys, a session key isn't derivable from the server's long-term private key. Even if that key is stolen later, past recorded traffic stays protected.

**What HTTPS does *not* protect against**
- **A compromised endpoint:** malware on your device or a malicious browser extension can read the password before it's encrypted.
- **Phishing:** HTTPS proves the connection is encrypted to *that domain*, not that the domain is the real one you meant to visit. A lookalike domain can have a valid certificate too.
- **Weak server-side storage:** HTTPS protects the password *in transit*. The site must still hash it (with bcrypt, scrypt, or Argon2) rather than store it in plain text. If the server is breached, that's what protects you.
- **Stripping on first contact:** if you type `http://` or the site lacks HSTS, an attacker on the network could downgrade the connection. HSTS and HTTPS-only browsing help prevent this.

**Practical steps that complement HTTPS**
- Use a password manager, which fills credentials only on the exact domain it's saved for.
- Enable two-factor authentication.
- Check the address bar for the correct domain before logging in.
- Use unique passwords for every site.
