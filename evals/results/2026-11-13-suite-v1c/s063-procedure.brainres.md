<!-- Q: 맥에서 파이썬 가상환경 만드는 법 알려주세요. -->

`python3 -m venv .venv`로 프로젝트 폴더 안에 가상환경을 만들 수 있어요. 별도 설치는 필요 없어요. venv는 파이썬에 기본으로 들어 있어요.

**예시 (프로젝트 폴더 `myproject`):**

```zsh
cd myproject
python3 -m venv .venv      # 가상환경 생성
source .venv/bin/activate  # 활성화
pip install requests       # 이 환경에만 설치됨
deactivate                 # 종료
```

활성화되면 프롬프트 앞에 `(.venv)`가 붙어요. 이때 `which python`이 `.venv/bin/python`을 가리키면 제대로 된 거예요.

맥에서 자주 겪는 문제 두 가지가 있어요.

- `python` 명령이 없다고 나오면 `python3`을 쓰세요. 활성화한 뒤에는 `python`도 동작해요.
- `python3`가 없다고 나오면 `brew install python`으로 설치하세요. 또는 python.org 설치 파일을 써도 돼요.

git을 쓴다면 `.gitignore`에 `.venv/`를 추가하세요. 패키지 목록은 `pip freeze > requirements.txt`로 저장하고, 다른 곳에서는 `pip install -r requirements.txt`로 복원해요.

원하시면 이 작업 폴더에 직접 만들어 드릴게요.
