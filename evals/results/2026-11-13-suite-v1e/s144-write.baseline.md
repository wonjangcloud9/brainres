<!-- Q: 파이썬으로 CSV 파일을 읽어서 숫자 열마다 평균을 구하는 코드 짜줘. -->

pandas 없이 표준 라이브러리만 사용한 버전입니다. 숫자가 아닌 값은 건너뛰고, 숫자가 하나도 없는 열은 제외합니다.

```python
import csv
import sys
from collections import defaultdict


def column_means(path, encoding="utf-8-sig"):
    sums = defaultdict(float)
    counts = defaultdict(int)

    with open(path, newline="", encoding=encoding) as f:
        reader = csv.DictReader(f)
        for row in reader:
            for col, value in row.items():
                if value is None or value.strip() == "":
                    continue
                try:
                    num = float(value.replace(",", ""))
                except ValueError:
                    continue  # 숫자가 아닌 값은 무시
                sums[col] += num
                counts[col] += 1

    return {col: sums[col] / counts[col] for col in counts}


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "data.csv"
    for col, mean in column_means(path).items():
        print(f"{col}: {mean:.4f}")
```

사용법:

```bash
python mean.py data.csv
```

참고:
- `utf-8-sig`는 엑셀에서 저장한 CSV의 BOM을 처리합니다. 한글 CSV가 깨지면 `encoding="cp949"`로 바꿔 보세요.
- `1,234`처럼 천 단위 쉼표가 있는 값도 숫자로 처리합니다.
- 문자열 열에 숫자가 섞여 있으면 그 숫자만 평균에 들어가므로, 열 타입이 확실하다면 검증 로직을 추가하는 게 좋습니다.

pandas 버전이 필요하면 아래처럼 한 줄로도 가능합니다:

```python
import pandas as pd
print(pd.read_csv("data.csv").mean(numeric_only=True))
```
