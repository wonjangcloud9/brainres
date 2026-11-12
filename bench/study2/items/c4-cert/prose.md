<!-- Q: Why does HTTPS need a certificate if it already encrypts traffic? -->

Encryption alone only guarantees that nobody can read the traffic between you and *whoever* is on the other end. An attacker could set up their own encrypted connection and pretend to be your bank. The certificate proves the other end really is your bank, because a trusted authority signed it for that domain. So encryption keeps the conversation private, and the certificate makes sure it's with the right party.
