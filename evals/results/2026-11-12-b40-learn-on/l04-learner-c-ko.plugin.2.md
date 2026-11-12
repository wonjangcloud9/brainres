<!-- Q: C 배우는 중이에요. 평균을 구하는데 소수점이 안 나와요.

```c
int sum = 7;
int n = 2;
double avg = sum / n;
printf("%f\n", avg);
``` -->

`sum / n`은 `int`끼리 나눠서 먼저 `3`이 되고, 그 `3`이 `double`로 바뀌어 `3.000000`이 나와요.

나눗셈 결과의 타입은 오른쪽 계산에서 정해져요. 왼쪽이 `double`이어도 소용없어요. 둘 다 `int`이면 소수점 아래를 버려요.

한 줄만 고치면 돼요. 피연산자 하나를 `double`로 바꾸세요.

```c
double avg = (double)sum / n;   // 7.0 / 2 → 3.5
printf("%f\n", avg);            // 3.500000
```

`(double)sum`은 `sum`의 값을 `double`로 바꿔요. 그러면 `n`도 자동으로 `double`이 되어 실수 나눗셈이 돼요. 주의할 점은 괄호 위치예요. `(double)(sum / n)`으로 쓰면 이미 `3`이 된 뒤에 바꾸니까 똑같이 `3.0`이에요.

바로 확인해 볼 질문이에요. `double avg = (double)(sum / n);`을 실행하면 무엇이 출력될까요?
