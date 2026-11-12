<!-- Q: 맥에서 파이썬 가상환경 만드는 법 알려주세요. -->

맥에서 `venv`(파이썬 기본 내장)로 가상환경을 만드는 방법입니다.

## 1. 파이썬 확인

```bash
python3 --version
```

설치되어 있지 않다면 Homebrew로 설치합니다.

```bash
brew install python
```

## 2. 가상환경 생성

프로젝트 폴더로 이동한 뒤 실행합니다.

```bash
cd 내프로젝트폴더
python3 -m venv .venv
```

`.venv`는 가상환경이 저장될 폴더 이름입니다(원하는 이름으로 바꿔도 됩니다).

## 3. 활성화

```bash
source .venv/bin/activate
```

활성화되면 프롬프트 앞에 `(.venv)`가 표시됩니다.

## 4. 패키지 설치 및 사용

```bash
pip install requests
pip list
```

이 패키지들은 해당 가상환경 안에만 설치됩니다.

## 5. 비활성화

```bash
deactivate
```

## 추가 팁

- **의존성 저장/복원**
  ```bash
  pip freeze > requirements.txt     # 저장
  pip install -r requirements.txt   # 다른 환경에서 복원
  ```
- **삭제**: 폴더만 지우면 됩니다. `rm -rf .venv`
- **Git 사용 시**: `.gitignore`에 `.venv/`를 추가하세요.
- **특정 파이썬 버전 사용**: `python3.12 -m venv .venv`처럼 버전을 지정합니다.
- **더 빠른 대안**: `uv`를 쓰면 훨씬 빠릅니다.
  ```bash
  brew install uv
  uv venv
  source .venv/bin/activate
  uv pip install requests
  ```

원하시면 현재 작업 폴더에 직접 만들어 드릴 수도 있습니다.
