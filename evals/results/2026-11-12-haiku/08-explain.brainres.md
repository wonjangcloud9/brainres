<!-- Q: Explain how HTTPS keeps my password safe. -->

HTTPS protects your password by encrypting the connection between your browser and the website, so anyone watching the network sees only scrambled data.

Here is how it works, in three steps:

1. **Handshake:** Your browser and the server agree on encryption keys using TLS. The server proves its identity with a certificate signed by a trusted authority, so your browser knows it's talking to the real site and not an impostor.
2. **Encryption:** Once the handshake finishes, everything your browser sends, including the password in a login form, gets encrypted with those keys before it leaves your device.
3. **Integrity:** Each message carries a check value. If someone alters a packet in transit, the check fails and the connection is dropped.

Two things HTTPS does not do:

- **It does not protect the password after it reaches the server.** The server must store it safely, usually as a salted hash, which is the site's job.
- **It does not stop phishing.** If you type your password into a fake site with a valid certificate, HTTPS encrypts it for the attacker. Check the domain name before you log in.

To confirm a site uses HTTPS, look for `https://` in the address bar and the lock icon. Never enter a password on a page that shows a warning.
