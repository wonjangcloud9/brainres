<!-- Q: Explain how HTTPS keeps my password safe. -->

# How HTTPS Protects Your Password

When you type your password into a login form and press submit, it travels from your device through many machines you don't control: your Wi-Fi router, your ISP, and various routers across the internet. Without protection, any of them could read it.

## Without HTTPS (plain HTTP)

The request is sent as readable text:

```
POST /login HTTP/1.1
Host: example.com

username=alice&password=hunter2
```

Anyone on the path, such as someone on the same coffee-shop Wi-Fi, could see `hunter2`.

## With HTTPS

HTTPS is HTTP running inside **TLS** (Transport Layer Security). TLS gives you three guarantees.

### 1. Authentication: you're talking to the real site

When you connect, the server sends a **certificate**. It says, in effect, "I am example.com, and here is my public key." A trusted **Certificate Authority (CA)** has digitally signed it.

Your browser:
- checks that the signature chains back to a CA it already trusts, since your OS and browser ship with a list of them,
- checks that the certificate matches the domain you typed and hasn't expired, and
- makes the server prove it holds the matching **private key**.

This stops an attacker from pretending to be the site. They can't produce a valid certificate for a domain they don't control.

### 2. Encryption: no one can read it

During the **TLS handshake**, your browser and the server use a key exchange method, usually Elliptic-Curve Diffie-Hellman (ECDHE), to agree on a shared secret key.

- An eavesdropper can watch the entire exchange and still can't work out the key. This is the mathematical core of the scheme.
- That key then encrypts everything with a fast symmetric cipher such as AES-GCM or ChaCha20.

Your password now looks like random bytes to anyone in the middle:

```
17 03 03 00 4a 8f 2c e1 9b 3d ... (gibberish)
```

### 3. Integrity: no one can change it

Each encrypted message carries an authentication tag. If anyone modifies even one bit in transit, the tag check fails and the connection is dropped. An attacker can't inject scripts into the login page or alter what you send.

### Bonus: forward secrecy

Modern TLS creates fresh keys for every session and then throws them away. Even if the server's private key is stolen years later, recorded past traffic still can't be decrypted.

## What HTTPS does *not* protect against

HTTPS only protects data **in transit**. It doesn't help in these cases:

| Threat | Why HTTPS doesn't help |
|---|---|
| **Phishing sites** | `examp1e-login.com` can get a valid certificate too. The padlock means "encrypted connection," not "trustworthy site." Check the domain. |
| **Malware or keyloggers on your device** | They capture the password before it is encrypted. |
| **Poor storage on the server** | Once the password arrives, the server decrypts it. Whether it's stored safely, ideally hashed with bcrypt, scrypt, or Argon2, is up to the site. |
| **Breaches at the site** | If the server is compromised, the attacker sees what the server sees. |
| **Reused passwords** | If one site leaks your password, HTTPS elsewhere won't stop attackers from trying it on other sites. |

Some information also stays visible on the network. Observers can see **which domain** you're connecting to and how much data is sent. The page path, form contents, cookies, and your password stay hidden.

## In short

> HTTPS makes sure you're talking to the real site (certificates), that no one can read what you send (encryption), and that no one can tamper with it (integrity). Use it together with unique passwords, a password manager, and two-factor authentication. Those cover the parts HTTPS can't.
