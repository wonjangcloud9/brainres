<!-- Q: 급해요 ㅠㅠ git reset --hard 해서 오늘 작업한 거 다 날아갔어요. 커밋은 안 했어요. -->

커밋도 `git add`도 안 한 변경은 git만으로 복구하기 어려워요. 하지만 에디터 기록과 `git add` 흔적에서 되살릴 가능성이 있어요.

**먼저 하지 말 것:** `git gc`, `git prune`, `git clean`은 실행하지 마세요. 남은 흔적이 지워질 수 있어요.

**순서대로 확인해요:**

1. **에디터 로컬 기록 (가장 유력해요)**
   - VS Code: 파일을 열고 Explorer 하단의 **Timeline** 패널을 보세요. 또는 `Cmd+Shift+P` → `Local History: Find Entry to Restore`를 실행하세요.
   - JetBrains: 파일 우클릭 → **Local History → Show History**를 누르세요.
2. **`git add`를 한 적이 있다면:** 저장소 폴더에서 `git fsck --lost-found`를 실행하세요. 나온 `dangling blob <해시>`마다 `git show <해시>`로 내용을 확인해 보세요. 파일로 저장하려면 `git show <해시> > 복구파일.txt`를 쓰세요.
3. **Time Machine이나 터미널 스크롤백:** 백업이 켜져 있으면 오늘 오전 버전을 복원할 수 있어요.
4. **새로 만든 파일(untracked):** `reset --hard`는 이 파일들을 지우지 않아요. 폴더에 그대로 있는지 `git status`로 보세요.

저는 지금 git 저장소가 아닌 임시 폴더에 있어서 제가 직접 확인하지는 못했어요. 저장소 경로를 알려주시면 `git fsck`를 대신 돌려서 복구할 파일을 찾아볼게요. 일단 1번부터 해보세요.
