<!-- Q: 파이썬으로 CSV 파일을 읽어서 숫자 열마다 평균을 구하는 코드 짜줘. -->

pandas를 쓰면 `mean(numeric_only=True)` 한 줄로 숫자 열만 골라 평균을 구해요.

```python
import sys
import pandas as pd

df = pd.read_csv(sys.argv[1])
print(df.mean(numeric_only=True))
```

실행은 `python mean_csv.py data.csv`처럼 해요. 예를 들어 `data.csv`가 아래와 같다면:

```
name,age,score
kim,30,80.5
lee,25,90
park,35,70
```

출력은 이렇게 나와요.

```
age      30.0
score    80.5
dtype: float64
```

`name`은 문자열이라 자동으로 빠져요.

pandas 없이 표준 라이브러리만 쓰고 싶다면 이 코드를 써요.

```python
import csv
import sys

sums, counts = {}, {}
with open(sys.argv[1], newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        for col, val in row.items():
            try:
                x = float(val)
            except (ValueError, TypeError):
                continue  # 숫자가 아닌 칸은 건너뜀
            sums[col] = sums.get(col, 0.0) + x
            counts[col] = counts.get(col, 0) + 1

for col in sums:
    print(f"{col}: {sums[col] / counts[col]}")
```

주의할 점이 두 가지 있어요.
- pandas는 `1,234`처럼 쉼표가 든 값을 문자열로 읽어서 평균에서 빠져요. 이때는 `read_csv(..., thousands=",")`를 써요.
- 표준 라이브러리 버전은 비어 있거나 숫자가 아닌 칸을 건너뛰어요. 그래서 열마다 평균을 낸 행 수가 달라질 수 있어요.

한글이 깨지면 `encoding="cp949"`를 지정해 보세요. 원하면 이 파일을 작업 폴더에 만들어 드릴게요.
