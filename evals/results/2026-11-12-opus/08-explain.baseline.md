<!-- Q: Explain how HTTPS keeps my password safe. -->

# How HTTPS Protects Your Password

When you type your password into a login form and hit "Sign in," HTTPS (HTTP over TLS) makes sure that only the real website can read it, and that nobody can tamper with it along the way.

## The problem it solves

Your password travels through many machines you don't control: your Wi-Fi router, your ISP, backbone routers, and possibly a coffee shop's network. With plain HTTP, every one of them sees your password in **plain text**. Anyone sniffing the network (for example, someone else on public Wi-Fi) could read it directly.

## What HTTPS does

### 1. It verifies you're talking to the real site (authentication)
When your browser connects, the server presents a **certificate**. The certificate says, in effect, "I am `bank.com`, and here is my public key." A trusted **Certificate Authority (CA)** has signed it.

- Your browser checks that signature against CAs it already trusts (these are built into your OS or browser).
- It confirms that the domain on the certificate matches the site you typed.
- If anything is off, you get the big red "Your connection is not private" warning.

This step stops an attacker from pretending to be the site and collecting your password themselves.

### 2. It agrees on a secret key (key exchange)
Your browser and the server run a **key exchange**, usually ECDHE (Elliptic-Curve Diffie-Hellman). The clever part is that both sides end up with the same secret **session key**, but that key is never sent over the network. An eavesdropper who sees every message still can't work it out.

Modern TLS also provides **forward secrecy**: each session gets a fresh key. Even if the server's long-term private key is stolen years later, recorded past traffic still can't be decrypted.

### 3. It encrypts everything (confidentiality)
All traffic is then encrypted with that session key using a fast symmetric cipher such as **AES-GCM** or **ChaCha20-Poly1305**. That includes your password, cookies, the URL path, and the page contents. On the wire, an observer sees only random-looking bytes.

### 4. It detects tampering (integrity)
Every encrypted record carries an authentication tag. If anyone changes even one bit in transit, the check fails and the connection is dropped. An attacker can't, for example, inject a script into the login page that steals your password.

## A simplified picture

```
You ──[ "hunter2" ]──► Coffee-shop Wi-Fi ──► ISP ──► bank.com
         HTTP:  everyone along the path reads "hunter2"

You ──[ 8f3a…c91e ]──► Coffee-shop Wi-Fi ──► ISP ──► bank.com
         HTTPS: only bank.com can decrypt it
```

## What HTTPS does *not* protect against

HTTPS secures the **trip**, not the endpoints:

- **Phishing sites.** `bank-login-secure.com` can have a perfectly valid certificate. The padlock means "encrypted to *this* domain," not "this site is trustworthy." Always check the domain.
- **Malware on your device.** A keylogger captures your password before it's ever encrypted.
- **What the server does with it.** Once your password arrives, it's decrypted. A well-run site then **hashes** it (with bcrypt, scrypt, or Argon2) instead of storing it as-is. HTTPS can't guarantee they do that.
- **Metadata.** Observers can still see *which* server you connect to (through its IP address and often the domain name) and how much data you send. They just can't see the contents.

## TL;DR
HTTPS proves you're talking to the real site through certificates. It then sets up a secret key that nobody else can derive, and uses that key to encrypt your password and check it for tampering. Anyone in between sees only gibberish. To stay safe, combine it with checking the domain name, a password manager (which won't autofill on fake domains), and two-factor authentication.
