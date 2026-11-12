<!-- Q: 깃에서 실수로 main 브랜치에 바로 커밋했어. 이 커밋을 새 브랜치로 옮기려면 어떻게 해? -->

아직 push 전이라면 아래 순서로 하면 됩니다.

## 커밋이 로컬에만 있을 때 (push 전)

```bash
# 1. 현재 main 상태(커밋 포함)에서 새 브랜치 생성
git branch my-feature

# 2. main을 원격 main 상태로 되돌림
git reset --hard origin/main

# 3. 새 브랜치로 이동
git switch my-feature
```

- `git branch my-feature`는 브랜치를 만들기만 하고 이동하지 않기 때문에, 방금 한 커밋이 새 브랜치에 그대로 남습니다.
- `git reset --hard origin/main`은 로컬 main을 원격과 같은 위치로 되돌립니다. 커밋은 `my-feature`에 있으니 사라지지 않습니다.

주의: `reset --hard`는 커밋되지 않은 작업 내용도 지웁니다. 작업 중인 변경사항이 있다면 먼저 `git stash`로 보관하거나 커밋하세요. 실행 전에 `git status`와 `git log --oneline -3`으로 상태를 확인해두면 안전합니다.

## 커밋을 여러 개 했거나 origin/main이 최신이 아닐 때

먼저 `git fetch`로 원격 정보를 갱신한 뒤 같은 방식으로 진행하세요. 몇 개의 커밋이 옮겨지는지 확인하려면:

```bash
git log origin/main..main --oneline
```

이 목록에 나오는 커밋들이 새 브랜치로 옮겨질 대상입니다.

## 이미 main에 push까지 했다면

원격 main이 보호되어 있지 않고 팀과 합의된 경우가 아니면 force push는 피하세요. 대신 새 브랜치에 커밋을 두고, main에는 `git revert <커밋해시>`로 되돌리는 커밋을 추가하는 것이 안전합니다.

참고로 현재 작업 디렉터리는 git 저장소가 아니라서 여기서 직접 실행하지는 않았습니다. 실제 저장소 경로에서 실행하시거나, 원하시면 해당 경로를 알려주세요.
