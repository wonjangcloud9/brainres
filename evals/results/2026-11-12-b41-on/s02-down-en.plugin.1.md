<!-- Q: Our site has been down for 20 minutes and I'm panicking. nginx says 502 Bad Gateway. -->

**Check your upstream app, not nginx: restarting nginx won't fix a 502, because nginx is working and can't reach the app behind it.**

Run these on the server, in order:

1. `sudo tail -n 50 /var/log/nginx/error.log` shows the reason. "connect() failed (111: Connection refused)" means the app is down. "No such file" on a socket means the app's socket is missing. "upstream timed out" means the app is hung.
2. `systemctl status <your-app>` (or `pm2 status` / `docker ps`) shows whether the app process is running. Common names are `gunicorn`, `php8.x-fpm`, `node`, `puma`.
3. If it's dead or hung, restart it: `sudo systemctl restart <your-app>`. Then reload the site.
4. If it dies again, check the app's logs with `journalctl -u <your-app> -n 100`. Look for `Out of memory` or `Killed`, and run `free -h` and `df -h`. A full disk or exhausted memory is the usual cause of an app that was fine and then stopped.
5. If the app is running but you still get 502, compare the `proxy_pass` or `fastcgi_pass` address in your nginx config with the port or socket the app actually listens on. Then run `sudo nginx -t`.

Run step 1 and paste the last few error lines here. I can tell you which case it is. I can't see your server from this session, so I'm working only from what you tell me.
