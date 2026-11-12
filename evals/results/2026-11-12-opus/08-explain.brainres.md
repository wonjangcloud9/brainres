<!-- Q: Explain how HTTPS keeps my password safe. -->

HTTPS encrypts your password on your device before it leaves, so anyone watching the network (public Wi‑Fi, your ISP, a router in between) sees only scrambled bytes.

## How it works

1. **Identity check.** The website sends a certificate, a digital ID signed by a certificate authority your browser already trusts. Your browser confirms the certificate matches the domain you typed. This stops an impostor from sitting in the middle and pretending to be the site.
2. **Key agreement.** Your browser and the server create a shared secret key using a method called Diffie‑Hellman. An eavesdropper can watch the whole exchange and still can't work out the key.
3. **Encryption.** Your password travels encrypted with that key, usually with AES. The encryption also detects tampering, so nobody can alter the data in transit without your browser noticing.
4. **Fresh keys each session.** This property is called forward secrecy. If someone records your traffic today and steals the server's key later, the recording stays unreadable.

## What HTTPS does not protect

The padlock means "encrypted to this domain." It does not mean "this domain is honest." Four gaps remain:

- **Phishing sites.** A fake site like `paypa1-login.com` can get a valid certificate too. HTTPS will happily encrypt your password straight to the attacker.
- **The server itself.** The site decrypts your password on arrival. After that, safety depends on the site storing it properly, as a slow hash like bcrypt or Argon2.
- **Your device.** Malware or a keylogger can capture what you type before encryption happens.
- **Reuse.** If one site leaks your password, every site that shares it is exposed.

## Next step

Use a password manager with a unique password for each site. It also helps against phishing, because it autofills only on the exact domain where you saved the password. Where a site offers passkeys, turn them on, because a passkey never sends a reusable secret at all.
