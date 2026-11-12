<!-- Q: Explain how HTTPS keeps my password safe. -->

HTTPS keeps your password safe by encrypting it before it leaves your device, so anyone watching the network sees only scrambled data.

**How it works, in 4 steps:**

1. **Handshake.** Your browser and the site agree on encryption settings using TLS (the protocol under HTTPS).
2. **Identity check.** The site shows a certificate signed by a trusted authority, so you know you're talking to the real site and not an impostor.
3. **Key exchange.** The two sides create a shared secret key. An eavesdropper can't derive it from the traffic, because the exchange uses public-key math (Diffie-Hellman).
4. **Encrypted traffic.** When you submit your password, it's encrypted with that key. Only the site can decrypt it. Any tampering is also detected.

**What it protects against:** Wi-Fi snoopers, your ISP, and anyone in between reading or altering your login.

**What it doesn't protect against:**
- Phishing: a fake site with a valid HTTPS certificate still gets your password.
- Malware or a keylogger on your device.
- A breach at the site itself, where passwords are stolen from their database.

So HTTPS secures the trip, not the destination. Next step: use a password manager, which gives each site a unique password and refuses to autofill on lookalike domains.
