<!-- Q: Explain how HTTPS keeps my password safe. -->

HTTPS keeps your password safe by encrypting it on your device before it leaves, so anyone watching the network (Wi-Fi owners, your ISP, someone on the same café network) sees only scrambled bytes.

It works in three steps:

1. **Identity check.** The site sends a certificate, which is a digital ID signed by a certificate authority your browser already trusts. Your browser checks that the certificate matches the domain you typed. This stops an impostor from posing as your bank.
2. **Key agreement.** Your browser and the server run a key exchange (TLS, usually ECDHE). Both sides compute the same secret session key, and that key never crosses the network. An eavesdropper who records the whole exchange still can't work it out.
3. **Encrypted traffic.** Your password, along with the rest of the request, is encrypted with that session key. Each message also carries an integrity check, so tampering in transit is detected and the connection fails.

A new session key is made for each connection. Even if someone recorded your traffic and later stole the server's long-term key, they still couldn't decrypt it. This is called forward secrecy.

**What HTTPS does not protect:**
- **Phishing.** On `paypa1.com` the connection is encrypted, but you're sending your password to the attacker.
- **Malware on your device.** A keylogger reads the password before it is encrypted.
- **The server itself.** After decryption, the site must store your password hashed. HTTPS says nothing about that, so a breached site can still leak it.

To check a site, look for the padlock and read the domain in the address bar. For extra safety, use a password manager, which won't autofill on a lookalike domain, and turn on two-factor authentication.
