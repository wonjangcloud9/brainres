<!-- Q: 도커 이미지랑 컨테이너 차이가 뭐고, 이미지 용량은 어떻게 줄여요? -->

이미지는 읽기 전용 설계도이고, 컨테이너는 그 이미지를 실행한 프로세스예요.

| | 이미지 | 컨테이너 |
|---|---|---|
| 상태 | 변하지 않아요 | 실행 중 파일이 바뀌어요 |
| 구성 | 읽기 전용 레이어 묶음 | 이미지 위에 쓰기 레이어 하나 추가 |
| 관계 | 하나로 여러 개 실행해요 | 이미지 하나에서 여럿이 나와요 |
| 명령 | `docker build`, `docker pull` | `docker run`, `docker rm` |

## 이미지 용량 줄이는 방법

1. **작은 베이스 이미지**를 써요. `node:22` 대신 `node:22-alpine`이나 `-slim`을 골라요. alpine은 musl libc라서 네이티브 모듈이 깨질 수 있어요. 그럴 땐 `-slim`을 쓰세요.
2. **멀티 스테이지 빌드**를 써요. 빌드 도구는 버리고 결과물만 최종 이미지에 복사해요.
3. **`.dockerignore`**에 `node_modules`, `.git`, `*.log`를 적어요. 불필요한 파일이 빌드 컨텍스트에 안 들어가요.
4. **레이어를 합쳐요.** 설치와 캐시 삭제를 같은 `RUN`에 넣어요. 다른 `RUN`에서 지우면 앞 레이어에 파일이 남아요.

## 예시 (Node 앱)

```dockerfile
FROM node:22 AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:22-alpine
WORKDIR /app
COPY --from=build /app/dist ./dist
COPY package*.json ./
RUN npm ci --omit=dev && npm cache clean --force
CMD ["node", "dist/index.js"]
```

최종 이미지에는 빌드용 devDependencies와 소스가 없어요.

먼저 `docker history <이미지>`를 실행해 가장 큰 레이어를 찾아보세요. 줄일 곳이 바로 보여요.
