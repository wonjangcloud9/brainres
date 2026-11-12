<!-- Q: Our site has been down for 20 minutes and I'm panicking. nginx says 502 Bad Gateway. -->

A 502 means nginx is running but can't get a response from your app server (Node, PHP-FPM, gunicorn, etc.), so the app process has almost certainly crashed or hung. Restarting it is usually the fastest fix.

Run these on the server, in order:

1. **See why nginx failed:** `sudo tail -n 50 /var/log/nginx/error.log`. Look for `connect() failed (111: Connection refused)` (app is down), `No such file or directory` (a socket is missing), or `upstream timed out` (app is hung).
2. **Check the app service:** `systemctl status <your-app>`. If you use PHP, the service is `php-fpm` or `php8.x-fpm`. For Docker, use `docker ps -a`. For pm2, use `pm2 status`.
3. **Restart it:** `sudo systemctl restart <your-app>`, then reload the site.
4. **If it dies again, find out why:** `journalctl -u <your-app> -n 100 --no-pager`. The usual causes are out-of-memory kills (`dmesg | grep -i oom`), a full disk (`df -h`), or a bad deploy.

Did you deploy or change anything in the last hour? If so, roll that back first, because it's the most likely cause.

I can't see your server from here. Paste the output of steps 1 and 2 and I'll tell you exactly what's wrong.
