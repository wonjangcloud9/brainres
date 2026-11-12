<!-- Q: Explain how HTTPS keeps my password safe. -->

HTTPS keeps your password safe by encrypting it between your browser and the website, so anyone on the network path (Wi-Fi owner, ISP, an attacker on the same café network) sees only scrambled bytes.

It does this in three steps:

1. **Identity check.** The site sends a certificate, which is a signed statement that "this public key belongs to example.com". Your browser trusts it only if a certificate authority it already knows signed it. This stops an impostor from posing as the site.
2. **Key agreement.** Your browser and the server run a handshake (TLS) to create a shared secret key. The math (Diffie-Hellman) lets both sides compute the same key without ever sending it, so a eavesdropper who records the whole handshake still cannot derive it.
3. **Encrypted traffic.** Your password and everything else is encrypted with that key, and each message carries an integrity check. Tampering in transit is detected and the connection is dropped.

Without HTTPS (plain HTTP), the password travels as readable text, so anyone on the path can copy it.

**What HTTPS does not protect:**

- **The site itself.** If the server stores your password badly or gets breached, HTTPS does not help.
- **Phishing.** A fake site such as `examp1e.com` can have a valid certificate too. Check the domain.
- **Your device.** Malware or a keylogger sees the password before it is encrypted.

To check a site, click the padlock in the address bar and confirm the domain name matches what you intended. Then use a password manager, which fills passwords only on the exact saved domain and so helps against phishing.
