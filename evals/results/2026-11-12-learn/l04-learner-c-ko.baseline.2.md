<!-- Q: C 배우는 중이에요. 평균을 구하는데 소수점이 안 나와요.

```c
int sum = 7;
int n = 2;
double avg = sum / n;
printf("%f\n", avg);
``` -->

원인은 **정수 나눗셈**이에요. `sum`과 `n`이 둘 다 `int`라서 `sum / n`은 `double`에 대입되기 *전에* 이미 정수 연산으로 계산돼요.

- `7 / 2` → `3` (소수점 버려짐)
- 그 `3`이 `double`로 변환 → `3.000000`

`double avg`로 받는다고 해서 나눗셈 자체가 실수로 바뀌지는 않아요.

## 해결 방법

피연산자 중 하나 이상을 `double`로 바꿔 주세요.

```c
// 1) 형변환 (가장 흔한 방법)
double avg = (double)sum / n;

// 2) 실수 리터럴 곱하기
double avg = sum / (double)n;

// 3) 변수 자체를 double로
double sum = 7;
int n = 2;
double avg = sum / n;
```

결과:

```
3.500000
```

## 주의할 점

```c
double avg = (double)(sum / n);   // ❌ 틀림: 나눗셈을 먼저 하고 나서 변환
double avg = (double)sum / n;     // ✅ 맞음: sum을 먼저 변환
```

형변환 `(double)`은 바로 뒤의 `sum`에만 적용되고, 괄호로 묶으면 이미 정수 나눗셈이 끝난 뒤에 변환돼서 소용이 없어요.
