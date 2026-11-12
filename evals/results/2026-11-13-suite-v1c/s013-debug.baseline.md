<!-- Q: 도커 컨테이너 띄우려는데 'port is already allocated' 에러가 나요. -->

'port is already allocated'는 호스트의 해당 포트를 이미 다른 컨테이너나 프로세스가 쓰고 있다는 뜻입니다. 아래 순서로 확인해 보세요.

**1. 어떤 컨테이너가 그 포트를 쓰는지 확인**
```bash
docker ps --format "table {{.ID}}\t{{.Names}}\t{{.Ports}}"
```
중지된 컨테이너가 아니라 실행 중인 컨테이너만 포트를 점유합니다. 해당 컨테이너가 있으면:
```bash
docker stop <컨테이너명>   # 또는 docker rm -f <컨테이너명>
```

**2. 컨테이너가 아니라 호스트 프로세스가 쓰는 경우 (macOS)**
```bash
lsof -nP -iTCP:<포트번호> -sTCP:LISTEN
```
PID가 나오면 필요 시 `kill <PID>`로 종료합니다. (macOS에서는 AirPlay Receiver가 5000, 7000번 포트를 쓰는 경우가 많습니다. 시스템 설정 → 일반 → AirDrop 및 Handoff에서 끌 수 있어요.)

**3. 아무것도 안 보이는데 계속 에러가 나는 경우**
- docker compose로 띄웠다면: `docker compose down` 후 다시 `up`
- Docker Desktop 재시작 (좀비 포트 매핑이 남는 경우가 있습니다)

**4. 그냥 다른 포트를 쓰고 싶다면**
```bash
docker run -p 8081:80 ...   # 호스트 포트만 변경 (호스트:컨테이너)
```
compose라면 `ports:`의 앞쪽 숫자를 바꾸면 됩니다.

어떤 포트에서 충돌이 났는지, 실행한 명령(또는 compose 파일)을 알려주시면 더 구체적으로 짚어드릴게요.
