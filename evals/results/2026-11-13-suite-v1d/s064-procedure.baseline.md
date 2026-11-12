<!-- Q: Nginx로 리버스 프록시 설정하는 방법 알려줘. -->

# Nginx 리버스 프록시 설정

## 1. 설치

```bash
# macOS
brew install nginx

# Ubuntu/Debian
sudo apt install nginx
```

## 2. 기본 설정

설정 파일 위치:
- macOS(Homebrew): `/opt/homebrew/etc/nginx/nginx.conf` (Intel은 `/usr/local/etc/nginx/`)
- Linux: `/etc/nginx/conf.d/myapp.conf` 또는 `/etc/nginx/sites-available/`

```nginx
server {
    listen 80;
    server_name example.com;

    location / {
        proxy_pass http://127.0.0.1:3000;   # 백엔드 앱 주소

        proxy_set_header Host              $host;
        proxy_set_header X-Real-IP         $remote_addr;
        proxy_set_header X-Forwarded-For   $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

각 헤더의 역할:
- `Host`: 원래 요청된 도메인을 백엔드에 전달
- `X-Real-IP` / `X-Forwarded-For`: 클라이언트의 실제 IP 전달
- `X-Forwarded-Proto`: 원래 프로토콜(http/https) 전달

## 3. 적용

```bash
sudo nginx -t              # 문법 검사
sudo nginx -s reload       # 재로드 (Linux: sudo systemctl reload nginx)
```

Linux에서 `sites-available`을 쓴다면 먼저 심볼릭 링크가 필요합니다:
```bash
sudo ln -s /etc/nginx/sites-available/myapp /etc/nginx/sites-enabled/
```

## 4. 자주 쓰는 추가 설정

**경로별로 다른 백엔드로 보내기**
```nginx
location /api/ {
    proxy_pass http://127.0.0.1:8080/;   # 끝의 / 주의: /api/ 접두사가 제거됨
}
location / {
    proxy_pass http://127.0.0.1:3000;
}
```

**WebSocket 지원**
```nginx
location /ws/ {
    proxy_pass http://127.0.0.1:3000;
    proxy_http_version 1.1;
    proxy_set_header Upgrade    $http_upgrade;
    proxy_set_header Connection "upgrade";
}
```

**타임아웃 / 업로드 크기**
```nginx
proxy_read_timeout 60s;
client_max_body_size 50m;
```

**로드밸런싱**
```nginx
upstream backend {
    server 127.0.0.1:3000;
    server 127.0.0.1:3001;
}
server {
    location / { proxy_pass http://backend; }
}
```

## 5. HTTPS (Let's Encrypt)

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d example.com
```

certbot이 인증서 발급과 80→443 리다이렉트 설정까지 자동으로 처리하고, 자동 갱신도 등록해 줍니다.

## 6. 문제 해결

| 증상 | 확인할 것 |
|---|---|
| 502 Bad Gateway | 백엔드가 실행 중인지, 포트가 맞는지 |
| 504 Gateway Timeout | `proxy_read_timeout` 늘리기, 백엔드 응답 속도 확인 |
| 413 Request Entity Too Large | `client_max_body_size` 증가 |
| 설정 오류 | `/var/log/nginx/error.log` 확인 |

원하시면 특정 환경(Docker, Node/Spring/Django 등)에 맞춘 설정이나 현재 디렉터리에 설정 파일을 직접 만들어 드릴 수도 있습니다.
