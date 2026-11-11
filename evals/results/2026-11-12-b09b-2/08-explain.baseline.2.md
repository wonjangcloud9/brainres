<!-- Q: Explain how HTTPS keeps my password safe. -->

HTTPS wraps your HTTP traffic in TLS (Transport Layer Security), which protects your password in three ways: it keeps it secret, it makes sure you're talking to the right server, and it detects tampering.

## 1. Authentication: you're talking to the real site
When you connect, the server presents a **certificate** that binds its domain name to a public key. The certificate is signed by a Certificate Authority (CA) that your browser or OS already trusts. Your browser checks that:
- the signature chains back to a trusted CA,
- the domain matches the one you typed,
- the certificate hasn't expired or been revoked.

This stops someone from impersonating the site and collecting your password.

## 2. Key exchange: agreeing on a secret over an open network
Client and server run a handshake (in TLS 1.3, ephemeral Diffie-Hellman) to derive a shared session key. Eavesdroppers see the handshake messages but can't compute the key. Because the keys are ephemeral, recorded traffic can't be decrypted later even if the server's long-term private key leaks (**forward secrecy**).

## 3. Encryption and integrity: protecting the data itself
Everything after the handshake, including the URL path, headers, cookies, and your login form's POST body, is encrypted with a symmetric cipher (e.g., AES-GCM or ChaCha20-Poly1305). These are **authenticated** ciphers, so any modification in transit is detected and the connection is dropped.

Someone on the same Wi-Fi or at your ISP sees only that you're connecting to a given host (via the IP and usually the SNI field), plus the approximate amount of data, not your password.

## What HTTPS does *not* protect against
- **The site itself**: the server receives your plaintext password. Good sites hash it (bcrypt, scrypt, Argon2), but HTTPS doesn't ensure they do.
- **Phishing**: a fraudulent site like `paypa1.com` can have a valid certificate. HTTPS proves *who you're connected to*, not that they're trustworthy.
- **Malware or malicious extensions** on your device, which see the password before it's encrypted.
- **Weak or reused passwords**, which are still vulnerable if the site is breached.
- **Compromised or misissued CAs**, though Certificate Transparency logs make this much easier to detect.

## Practical takeaways
- Check that the domain is correct and the padlock is present before entering credentials.
- Use a password manager, which also helps defend against phishing since it won't autofill on lookalike domains.
- Enable multi-factor authentication, so a stolen password alone isn't enough.

I can go deeper on any part, such as the TLS 1.3 handshake step by step, if you'd like.
