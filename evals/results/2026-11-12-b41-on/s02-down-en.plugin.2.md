<!-- Q: Our site has been down for 20 minutes and I'm panicking. nginx says 502 Bad Gateway. -->

**Run `sudo tail -n 50 /var/log/nginx/error.log` on the server now.** It names the broken upstream (your app), and that tells you what to restart.

Restarting nginx won't help. A 502 means nginx is running fine but can't get an answer from the app behind it (gunicorn, php-fpm, node, etc.).

1. In the log, look for `connect() failed (111: Connection refused)` or `upstream prematurely closed`. Note the address or socket after `upstream:`.
2. Check the app service, using your service's name: `sudo systemctl status <app>`. If it's dead, run `sudo systemctl restart <app>`.
3. Reload the site. If it works, you're back up.
4. If the app dies again, run `sudo journalctl -u <app> -n 100`, `df -h` and `dmesg | grep -i kill`. A full disk or an out-of-memory kill is the usual cause.
5. If it started right after a deploy or config change, roll that back and run `sudo nginx -t`.

I can't see your server from this session, so I don't know which app you run. Paste the error log lines or the `status` output here and I'll tell you the exact fix.
