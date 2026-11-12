<!-- Q: Explain how HTTPS keeps my password safe. -->

HTTPS keeps your password safe by encrypting it between your browser and the website, so anyone on the network path (Wi-Fi owner, ISP, a router in between) sees only scrambled bytes.

It does this in three steps:

1. **Identity check.** The site sends a certificate. Your browser checks that a trusted authority signed it for that exact domain. This stops an impostor from posing as the site, because the impostor can't produce a valid certificate for a domain they don't control.
2. **Key agreement.** Your browser and the server run a key exchange (in TLS 1.3, an ephemeral Diffie-Hellman exchange). Both sides end up with the same secret key, and that key never crosses the network. An eavesdropper who records everything still can't derive it.
3. **Encrypted, tamper-proof traffic.** Your password travels inside messages encrypted with that key (AES or ChaCha20). Each message also carries an integrity check, so an attacker can't alter it without detection.

Without HTTPS, plain HTTP sends the password as readable text, and anyone on the same café Wi-Fi could read it.

HTTPS does **not** protect against these:
- **Phishing.** A fake site like `paypa1.com` can have a valid certificate for its own domain. Check the address bar.
- **Malware or keyloggers** on your device, which read the password before it's encrypted.
- **Server-side breaches.** The site decrypts your password on arrival. If it stores the password badly, HTTPS doesn't help. Good sites store only a salted hash.
- **Reuse.** A leaked password from one site works on others.

To stay safe, check for the padlock and the correct domain, use a password manager (it won't autofill on a lookalike domain), and turn on two-factor authentication.
