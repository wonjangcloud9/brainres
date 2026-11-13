<!-- Q: Nginx로 리버스 프록시 설정하는 방법 알려줘. -->

`proxy_pass`로 백엔드 주소를 지정하면 Nginx가 리버스 프록시로 동작해요. 예를 들어 `app.example.com`으로 오는 요청을 `localhost:3000`의 앱으로 넘기는 설정은 이래요.

```nginx
# /etc/nginx/conf.d/app.conf (macOS Homebrew는 /opt/homebrew/etc/nginx/servers/app.conf)
server {
    listen 80;
    server_name app.example.com;

    location / {
        proxy_pass http://127.0.0.1:3000;

        proxy_set_header Host              $host;
        proxy_set_header X-Real-IP         $remote_addr;
        proxy_set_header X-Forwarded-For   $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

적용 순서는 이래요.

1. 설정 파일을 위 경로에 저장해요.
2. `sudo nginx -t`로 문법을 검사해요.
3. `sudo nginx -s reload`로 반영해요.
4. `curl -H "Host: app.example.com" http://127.0.0.1/`로 응답을 확인해요.

각 헤더의 역할은 이래요.

| 헤더 | 역할 |
|---|---|
| `Host` | 원래 요청 도메인을 백엔드에 전달해요 |
| `X-Real-IP` | 클라이언트 IP를 전달해요 |
| `X-Forwarded-For` | 프록시를 거친 IP 목록을 전달해요 |
| `X-Forwarded-Proto` | 원래 프로토콜(http/https)을 전달해요 |

WebSocket을 쓰면 `location` 안에 아래 세 줄을 추가해야 해요. 없으면 연결이 끊겨요.

```nginx
proxy_http_version 1.1;
proxy_set_header Upgrade    $http_upgrade;
proxy_set_header Connection "upgrade";
```

HTTPS는 `listen 443 ssl;`과 인증서 경로를 추가하면 돼요. Let's Encrypt를 쓰면 `sudo certbot --nginx -d app.example.com`이 설정을 자동으로 고쳐줘요.

백엔드 포트, 도메인, HTTPS 여부를 알려주면 그 값으로 완성된 설정 파일을 만들어 드릴게요.
