<!-- Q: Explain how HTTPS keeps my password safe. -->

HTTPS wraps your HTTP traffic in TLS (Transport Layer Security). Here's how that protects a password you type into a login form.

## 1. Authenticating the server (certificates)
When your browser connects, the server presents a **certificate** that says "I am example.com," signed by a Certificate Authority (CA) your device already trusts. The browser verifies:
- The signature chains up to a trusted root CA
- The domain name matches
- The certificate hasn't expired or been revoked

This stops an attacker from impersonating the site and collecting your password.

## 2. Agreeing on a secret key (handshake)
Browser and server use a key exchange (modern TLS uses ephemeral Diffie-Hellman, e.g. X25519) to derive a shared secret **without ever sending it over the wire**. An eavesdropper watching the entire handshake still can't compute it. The server proves it owns the certificate by signing handshake data with its private key.

Because the keys are ephemeral, recording traffic today and stealing the server's key later doesn't let anyone decrypt it (**forward secrecy**).

## 3. Encrypting everything
Once the shared key exists, all data, including the URL path, headers, cookies, and your POSTed password, is encrypted with a symmetric cipher such as AES-GCM or ChaCha20-Poly1305. These also include an **authentication tag**, so any tampering in transit is detected.

## What an attacker on the network sees
Someone on the same Wi-Fi or at your ISP can see the destination domain (via DNS/SNI) and traffic volume, but not the password, page content, or cookies.

## What HTTPS does *not* protect against
- **Phishing**: a lookalike domain can have a perfectly valid certificate. Check the URL.
- **Malware or malicious extensions** on your device that read input before encryption.
- **A compromised or careless server**: HTTPS protects the password in transit only. Once it arrives, the site must store it safely (salted, slow hashes like bcrypt/argon2).
- **Weak or reused passwords**: use a password manager and 2FA.
- **Rogue root CAs** installed on your device (e.g. by corporate proxies or malware) can allow interception.

In short: HTTPS ensures you're talking to the real server, that nobody can read your password in transit, and that nobody can alter it along the way.
