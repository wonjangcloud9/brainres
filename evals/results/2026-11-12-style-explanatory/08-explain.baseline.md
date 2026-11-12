<!-- Q: Explain how HTTPS keeps my password safe. -->

HTTPS wraps your HTTP traffic in TLS (Transport Layer Security). When you submit a password, it's protected in three ways: it's encrypted, the server is verified, and tampering is detectable.

## The sequence

1. **Connection and hello.** Your browser tells the server which TLS versions and cipher suites it supports. The server picks one.

2. **Server proves its identity.** The server sends a certificate containing its public key and the domain name, signed by a Certificate Authority (CA) your OS/browser already trusts. Your browser checks that:
   - the signature chains up to a trusted root CA
   - the domain matches the one you typed
   - the certificate hasn't expired or been revoked

3. **Key exchange.** Browser and server use an ephemeral Diffie-Hellman exchange (usually ECDHE) to agree on a shared secret. An eavesdropper who sees the entire exchange still can't compute that secret. The server signs its part of the exchange with its certificate's private key, which proves it's the real owner of the certificate.

4. **Encrypted session.** Both sides derive symmetric session keys from the shared secret. Everything after this, including URLs paths, headers, cookies, and your POSTed password, is encrypted and authenticated with an AEAD cipher such as AES-GCM or ChaCha20-Poly1305.

## What each piece protects against

| Threat | Defense |
|---|---|
| Someone on your Wi-Fi reading the password | Symmetric encryption of all traffic |
| Someone modifying data in transit | AEAD authentication tags; any altered byte fails verification |
| A fake server impersonating the site (man-in-the-middle) | Certificate validation plus the signed key exchange |
| Someone recording traffic now and stealing the server key later | Forward secrecy: ephemeral keys are discarded, so past sessions can't be decrypted |

`★ Insight ─────────────────────────────────────`
- **Public-key crypto is only used to bootstrap.** Asymmetric operations are slow, so TLS uses them just to authenticate and agree on a key, then switches to fast symmetric encryption for the actual data.
- **The CA system is the trust anchor.** Encryption alone isn't enough: without certificate validation you could be encrypting perfectly to an attacker. That's why certificate warnings matter.
- **Forward secrecy comes from ephemeral keys.** Because the session key is never derived from the server's long-term key, compromising that key later doesn't expose recorded sessions.
`─────────────────────────────────────────────────`

## What HTTPS does *not* do

- **It doesn't protect the endpoints.** Malware on your device, a keylogger, or a compromised server still sees your password in plaintext.
- **It doesn't stop phishing.** `paypa1.com` can have a perfectly valid certificate. HTTPS proves you're talking to *that domain*, not that the domain is trustworthy.
- **The server still receives your plaintext password** after decrypting it. A well-built site then hashes it (bcrypt, scrypt, Argon2) before storing it, which is a separate protection from HTTPS.
- **It leaks some metadata.** Observers can usually see the domain (via SNI, unless ECH is used), the IP, and traffic volume and timing, but not the paths, parameters, or body.

## Practical takeaways

- Check that the domain is exactly what you intended, not just that there's a padlock.
- Don't click through certificate warnings on login pages.
- Use a password manager, which auto-fills only on the correct domain and helps against phishing.
- Use MFA or passkeys so a stolen password alone isn't enough.

If you're asking because you're implementing this, I can show you how to inspect a live handshake with `openssl s_client` or `curl -v`, or how to configure HTTPS on a server.
