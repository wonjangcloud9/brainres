<!-- Q: Explain how HTTPS keeps my password safe. -->

**HTTPS encrypts your password while it travels from your browser to the website, so anyone watching the network sees only scrambled bytes.** It does not protect the password once it reaches the server.

## How it works

HTTPS is ordinary web traffic (HTTP) wrapped in TLS, an encryption protocol. When you open a login page:

1. **The site proves its identity.** The server sends a certificate, a digital ID signed by a trusted certificate authority. Your browser checks the signature and confirms the certificate matches the domain you typed. This blocks an impostor posing as the real site.
2. **Both sides agree on a secret key.** They use a key exchange (usually ECDHE), so the shared key is never sent over the wire. An eavesdropper sees the exchange but can't compute the key.
3. **Everything is encrypted with that key.** Your password, cookies, and page content travel encrypted. Each message also carries an integrity check, so tampering in transit gets detected.
4. **Each session gets a fresh key.** This is called forward secrecy. Someone who steals the server's private key later still can't decrypt traffic they recorded earlier.

## What HTTPS doesn't cover

The padlock only means "encrypted connection to this domain," not "this site is honest." These gaps remain:

- **Phishing:** a fake site like `paypa1.com` can have valid HTTPS too.
- **Server storage:** the site decrypts your password on arrival. Safe storage depends on the site hashing it properly.
- **Your device:** malware or a keylogger reads the password before encryption happens.
- **Password reuse:** if one site leaks it, attackers try it everywhere.

## Next step

A password manager closes most of these gaps. It only autofills on the exact real domain, which defeats phishing. It also generates a unique password per site, which limits damage from leaks.
