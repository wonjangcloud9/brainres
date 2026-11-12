<!-- Q: C 배우는 중이에요. 평균을 구하는데 소수점이 안 나와요.

```c
int sum = 7;
int n = 2;
double avg = sum / n;
printf("%f\n", avg);
``` -->

`sum / n`은 `int`끼리 나누기라서 `7 / 2 = 3`이 먼저 나오고, 그 `3`이 `3.000000`으로 바뀌어 `avg`에 들어가요.

`double`에 담는 건 나눗셈이 끝난 뒤라서 소용이 없어요. 나누기 전에 피연산자 하나를 `double`로 바꿔야 해요.

```c
int sum = 7;
int n = 2;
double avg = (double)sum / n;   // 7.0 / 2 → 3.5
printf("%f\n", avg);            // 3.500000
```

`(double)sum`은 `sum`을 실수로 바꾸는 형변환이에요. 한쪽이 `double`이면 `n`도 자동으로 `double`이 되어 실수 나눗셈이 돼요.

주의할 점은 괄호 위치예요. `(double)(sum / n)`은 나눗셈을 먼저 해서 똑같이 `3.0`이 나와요.

다음에는 `sum`을 `double`로 선언하거나 `sum / 2.0`으로 써 보세요. 결과가 같은지 확인해 보면 원리가 더 잘 잡혀요.
