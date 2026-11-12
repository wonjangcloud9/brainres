<!-- Q: Explain how HTTPS keeps my password safe. -->

HTTPS keeps your password safe in transit by encrypting it between your browser and the website, so anyone on the network path (Wi-Fi owner, ISP, attacker at a café) sees only scrambled bytes.

It works in three parts, built on TLS (the protocol underneath HTTPS):

1. **Identity check.** The server sends a certificate, signed by a certificate authority your browser already trusts. Your browser checks that the certificate matches the domain, for example `example.com`. This stops an impostor from posing as the site on the network.
2. **Key agreement.** Browser and server run a key exchange (usually elliptic-curve Diffie-Hellman) to create a shared secret key. An eavesdropper who records the whole exchange still cannot compute that key.
3. **Encrypted traffic.** Everything after that, including the URL path, headers and the form body that holds your password, is encrypted with that key. It is also authenticated, so any tampering in transit is detected and the connection fails.

Without HTTPS, the login form would send `password=hunter2` as plain text that any device on the path could read.

HTTPS has limits. It protects only the trip, not the endpoints:

- **Phishing:** a fake site at `examp1e.com` can have a valid certificate too. Check the domain.
- **Malware on your device:** it can read the password before encryption.
- **The server side:** once the password arrives, the site must store it as a salted hash. A site that stores it in plain text can leak it in a breach.

Next step: use a password manager. It fills passwords only on the exact domain you saved, which defeats most phishing, and it gives each site a unique password so one breach doesn't spread.
