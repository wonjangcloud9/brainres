<!-- Q: 도커 이미지랑 컨테이너 차이가 뭐고, 이미지 용량은 어떻게 줄여요? -->

## 이미지 vs 컨테이너

| | 이미지 (Image) | 컨테이너 (Container) |
|---|---|---|
| 정체 | 읽기 전용 템플릿 (파일시스템 + 메타데이터) | 이미지를 실행한 프로세스 인스턴스 |
| 상태 | 불변, 레이어로 구성 | 이미지 위에 쓰기 가능한 레이어가 하나 추가됨 |
| 비유 | 클래스 / 설치 파일 | 객체(인스턴스) / 실행 중인 프로그램 |
| 개수 | 하나의 이미지로 | 여러 컨테이너 생성 가능 |

`docker run`을 하면 이미지로부터 컨테이너가 만들어지고, 컨테이너에서 생긴 변경사항은 컨테이너의 쓰기 레이어에만 저장됩니다. 컨테이너를 삭제하면 그 변경사항도 사라지고, 이미지는 그대로 남습니다.

## 이미지 용량 줄이는 방법

**1. 가벼운 베이스 이미지 사용**
```dockerfile
FROM python:3.12-slim     # python:3.12 보다 훨씬 작음
FROM node:22-alpine       # alpine 기반
```
더 극단적으로는 `distroless`나 `scratch`(Go 같은 정적 바이너리)도 있습니다. alpine은 musl libc라서 일부 패키지(특히 Python 네이티브 확장)에서 호환 문제가 있을 수 있으니 `-slim`이 무난합니다.

**2. 멀티 스테이지 빌드 (효과 가장 큼)**
빌드 도구는 빌드 단계에만 두고, 결과물만 최종 이미지로 복사합니다.
```dockerfile
FROM golang:1.23 AS build
WORKDIR /src
COPY . .
RUN CGO_ENABLED=0 go build -o /app

FROM gcr.io/distroless/static
COPY --from=build /app /app
ENTRYPOINT ["/app"]
```

**3. 같은 레이어 안에서 정리**
레이어는 쌓이기만 하므로, 다음 `RUN`에서 지워도 용량은 줄지 않습니다. 한 `RUN`에서 설치와 정리를 같이 하세요.
```dockerfile
RUN apt-get update \
 && apt-get install -y --no-install-recommends curl \
 && rm -rf /var/lib/apt/lists/*
```
pip은 `--no-cache-dir`을 사용합니다.

**4. `.dockerignore` 작성**
`.git`, `node_modules`, `*.log`, 테스트 데이터 등이 빌드 컨텍스트와 `COPY . .`로 들어가지 않게 합니다.

**5. 필요한 것만 설치**
- 운영 의존성만: `npm ci --omit=dev`, `pip install` 시 dev 패키지 제외
- `--no-install-recommends` 사용

**6. 레이어 순서 최적화**
자주 바뀌는 것(소스코드)은 뒤에, 안 바뀌는 것(의존성 설치)은 앞에 두면 캐시 효율이 좋아집니다. 용량보다는 빌드 속도에 도움이 됩니다.

## 확인 도구
```bash
docker images                 # 전체 크기 확인
docker history <image>        # 레이어별 크기
```
레이어별로 더 자세히 보려면 [dive](https://github.com/wagoodman/dive)가 유용합니다.

사용하는 언어/프레임워크를 알려주시면 Dockerfile을 직접 보고 구체적으로 줄여드릴 수 있습니다.
