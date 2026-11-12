<!-- Q: 급해요 ㅠㅠ git reset --hard 해서 오늘 작업한 거 다 날아갔어요. 커밋은 안 했어요. -->

git만으로는 add·커밋 안 한 수정은 대부분 복구가 안 돼요. 하지만 아래 방법으로 살릴 수 있어요. 위에서부터 순서대로 해보세요.

1. **에디터 로컬 히스토리**가 가장 가능성이 커요. 에디터가 git과 별개로 저장본을 갖고 있어서예요.
   - VS Code: 파일을 열고 명령 팔레트(`Cmd+Shift+P`)에서 `Local History: Find Entry to Restore`를 실행해요. 탐색기 하단의 `Timeline` 패널도 확인해 보세요.
   - JetBrains: 파일이나 폴더를 우클릭하고 `Local History` → `Show History`를 선택해요.
2. **`git add`를 한 번이라도 했다면** 프로젝트 폴더에서 `git fsck --lost-found`를 실행해요. 그러면 `.git/lost-found/other/`에 파일 내용이 해시 이름으로 남아요. 열어서 내용을 확인하세요.
3. **Time Machine이나 클라우드 백업**(iCloud, Dropbox 버전 기록)에 오늘 저장본이 있을 수 있어요.
4. **새로 만든 파일**(untracked)은 `reset --hard`가 지우지 않아요. 폴더에 그대로 있는지 확인해 보세요.

복구하기 전에는 `git clean`이나 새 `reset`을 하지 마세요. 저장본을 덮어쓸 수 있어요.

지금 제 작업 폴더는 git 저장소가 아니라서 직접 확인은 못 했어요. 프로젝트 경로와 쓰는 에디터를 알려주시면 `fsck` 결과를 같이 확인해 드릴게요.
