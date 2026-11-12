<!-- Q: Our site has been down for 20 minutes and I'm panicking. nginx says 502 Bad Gateway. -->

**A 502 means nginx is running but can't get a response from your app server behind it, so the app process is almost certainly crashed, hung, or listening somewhere else.** I can't see your server from here, so run these on it in order:

1. Read why nginx failed: `sudo tail -n 50 /var/log/nginx/error.log`
   - `connect() failed (111: Connection refused)` means the app is down.
   - `connect() to unix:... failed (2: No such file)` means the socket is missing, so the app is down.
   - `upstream timed out` means the app is hung or overloaded.
   - `(13: Permission denied)` means a socket permission problem.
2. Check the app process. Use whichever fits your stack:
   - `systemctl status <your-app>` (or `pm2 status`, or `docker ps -a`)
   - `sudo journalctl -u <your-app> -n 100 --no-pager`
3. Restart it: `sudo systemctl restart <your-app>` (or `pm2 restart all`, or `docker restart <container>`). That usually restores the site within seconds.
4. If it dies again right away, check for these causes:
   - **Out of memory:** `dmesg -T | grep -i -E "killed process|out of memory"`
   - **Full disk:** `df -h`
   - **A bad deploy or config change:** check what changed about 20 minutes ago.

The 20-minute start time suggests a deploy, an OOM kill, or a full disk. Which of those fits is a guess until you've read the logs.

Paste the output of step 1 and the app's status here, and tell me your stack (Node, PHP-FPM, gunicorn, Docker?). I'll pinpoint the cause with you.
