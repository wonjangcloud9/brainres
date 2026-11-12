<!-- Q: CORS가 뭐야? 왜 브라우저에서만 막혀? -->

## CORS란?

**CORS (Cross-Origin Resource Sharing)** 는 한 출처(origin)의 웹 페이지가 **다른 출처**의 리소스를 요청할 때, 서버가 "허용한다"고 명시적으로 알려주는 브라우저 표준 메커니즘이에요.

**출처(origin)** = `프로토콜 + 도메인 + 포트`
- `https://myapp.com` → `https://api.myapp.com` : 다른 출처 (서브도메인 다름)
- `http://localhost:3000` → `http://localhost:8080` : 다른 출처 (포트 다름)
- `http://a.com` → `https://a.com` : 다른 출처 (프로토콜 다름)

## 왜 필요한가? (Same-Origin Policy)

브라우저는 기본적으로 **동일 출처 정책(SOP)** 을 적용해요. 이유는 보안 때문이에요.

예: 당신이 은행 사이트에 로그인한 상태에서 악성 사이트 `evil.com`을 열었다고 해볼게요. 브라우저는 은행 쿠키를 자동으로 붙여 요청을 보내기 때문에, `evil.com`의 JavaScript가 `bank.com/api/balance`를 호출해서 **응답을 읽을 수** 있다면 정보가 털립니다. SOP는 이걸 막아요.

CORS는 이 엄격한 규칙을 **서버가 선택적으로 풀어주는** 방법이에요.

## 왜 브라우저에서만 막힐까?

핵심: **CORS는 서버가 막는 게 아니라, 브라우저가 응답을 JS에 못 넘겨주는 것**이에요.

- `curl`, Postman, 서버-서버 호출에는 브라우저가 없으니 SOP/CORS 검사 자체가 없음
- 위험 시나리오는 "**사용자의 브라우저**가 사용자 쿠키/인증 정보를 들고 다른 사이트 요청을 대신 보내는 것"인데, 이건 브라우저에서만 발생
- 그래서 보호 장치도 브라우저에만 구현되어 있음

즉, CORS는 **서버 보호 장치가 아니라 사용자 보호 장치**예요. 공격자가 직접 curl로 호출하는 건 CORS로 못 막아요 (그건 인증/인가로 막아야 함).

## 동작 방식

**1. 단순 요청 (Simple request)**
GET/POST 등 단순한 요청은 바로 전송되고, 브라우저가 응답 헤더를 확인해요.

```
요청:  Origin: https://myapp.com
응답:  Access-Control-Allow-Origin: https://myapp.com
```
헤더가 없거나 불일치하면 → 요청은 서버에 **도달했지만** 브라우저가 JS에 응답을 안 넘겨줘요 (콘솔에 CORS 에러).

**2. Preflight 요청**
`PUT`/`DELETE`, `Content-Type: application/json`, 커스텀 헤더 등이 있으면 브라우저가 먼저 `OPTIONS` 요청을 보내 허용 여부를 물어봐요.

```
OPTIONS /api/users
Origin: https://myapp.com
Access-Control-Request-Method: PUT
Access-Control-Request-Headers: content-type

← 서버 응답
Access-Control-Allow-Origin: https://myapp.com
Access-Control-Allow-Methods: GET, PUT, POST
Access-Control-Allow-Headers: content-type
```
허용되면 실제 요청을 보내요.

## 흔한 해결법 (서버 쪽)

```js
// Express 예시
const cors = require('cors');
app.use(cors({
  origin: 'https://myapp.com',
  credentials: true,   // 쿠키 포함 시
}));
```

## 주의할 점

- `Access-Control-Allow-Origin: *` 는 **쿠키/인증정보 포함 요청(`credentials`)과 함께 못 씀**. 이 경우 구체적 origin을 명시해야 해요.
- 개발 중엔 프론트 dev server의 **proxy** 설정(Vite, CRA 등)으로 같은 출처처럼 보이게 우회할 수 있어요.
- 프론트에서 `mode: 'no-cors'`를 쓰면 에러는 사라지지만 응답을 **읽을 수 없는** opaque 응답이 돼서 보통 해결책이 아니에요.
- CORS 에러가 나도 서버엔 요청이 이미 도착해 처리됐을 수 있어요 (단순 요청의 경우). 그래서 상태 변경 API는 CSRF 방어가 별도로 필요해요.

특정 상황(예: React + Express, Spring, Nginx 설정)에서 겪고 있는 에러가 있으면 알려주세요, 거기에 맞춰 설명드릴게요.
