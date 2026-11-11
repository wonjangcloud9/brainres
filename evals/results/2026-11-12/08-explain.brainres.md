<!-- Q: Explain how HTTPS keeps my password safe. -->

HTTPS keeps your password safe by encrypting everything between your browser and the website, so anyone watching the network (Wi-Fi owner, ISP, an attacker on the same café network) sees only scrambled bytes instead of your password.

It works in three steps:

1. **Identity check.** The server sends a certificate, signed by a certificate authority your browser already trusts. Your browser verifies that the certificate matches the domain you typed. This stops an impostor from posing as the site.
2. **Key agreement.** Your browser and the server run a key exchange (in TLS 1.3, an ephemeral Diffie-Hellman exchange). Both sides end up with the same secret key, but that key never crosses the network, so an eavesdropper can't derive it from what they capture. Because the keys are ephemeral, recording the traffic today and stealing the server's key later still won't decrypt it.
3. **Encrypted, tamper-proof traffic.** Every request, including the one carrying your password, is encrypted with that shared key and carries an authentication tag. An attacker can't read the password, and any attempt to alter the data in transit makes the check fail and the connection drop.

What HTTPS does **not** protect against:

- **The site itself.** The server receives your password in readable form after decryption, so a site that stores it badly or gets breached still exposes it.
- **Your device.** Malware or a malicious browser extension can read the password before it's encrypted.
- **Phishing.** A lookalike domain like `paypa1.com` can have a valid certificate. HTTPS proves you reached *that domain*, not that it's the one you meant.

To see this yourself, click the padlock in your browser's address bar and open the certificate details. You'll see the domain, the issuing authority, and the expiry date.
