<!-- Q: Nginx로 리버스 프록시 설정하는 방법 알려줘. -->

`location` 블록에 `proxy_pass`를 넣으면 Nginx가 리버스 프록시로 동작해요. 아래는 `127.0.0.1:3000`에서 도는 앱을 `example.com`으로 노출하는 예시예요.

1. 설정 파일을 만들어요. Linux는 `/etc/nginx/conf.d/myapp.conf`, Homebrew(macOS)는 `/opt/homebrew/etc/nginx/servers/myapp.conf`예요.

```nginx
server {
    listen 80;
    server_name example.com;

    location / {
        proxy_pass http://127.0.0.1:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

2. 문법을 검사해요: `sudo nginx -t`
3. 설정을 다시 불러와요: `sudo nginx -s reload` (Linux는 `sudo systemctl reload nginx`도 돼요)
4. 확인해요: `curl -I http://example.com`

**주의할 점**
- `proxy_pass http://127.0.0.1:3000;`처럼 끝에 `/`가 없으면 요청 경로를 그대로 넘겨요. `/`를 붙이면 `location` 경로가 잘려서 전달돼요.
- `Host`와 `X-Forwarded-*` 헤더가 없으면 백엔드가 원래 도메인과 클라이언트 IP를 알 수 없어요.
- WebSocket을 쓰면 `location` 안에 아래 세 줄을 추가해요.

```nginx
proxy_http_version 1.1;
proxy_set_header Upgrade $http_upgrade;
proxy_set_header Connection "upgrade";
```

다음으로 HTTPS가 필요하면 `sudo certbot --nginx -d example.com`으로 인증서를 붙일 수 있어요. 실제 백엔드 포트나 도메인을 알려주면 설정을 맞춰서 써 드릴게요.
