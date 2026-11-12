<!-- Q: 급해요 ㅠㅠ git reset --hard 해서 오늘 작업한 거 다 날아갔어요. 커밋은 안 했어요. -->

**커밋도 `git add`도 안 한 파일이면 git으로는 복구할 수 없어요.** 하지만 `git add`를 한 번이라도 했다면 복구할 수 있어요. 아래 순서로 해 보세요.

1. **스테이징했던 파일 복구** (프로젝트 폴더에서 실행해요)
   ```
   git fsck --lost-found
   ```
   `dangling blob 해시`가 나오면 `git show <해시>`로 내용을 확인해요. 파일로 저장하려면 `git show <해시> > recovered.txt`를 쓰세요. `.git/lost-found/other/`에도 복사돼요.

2. **에디터 로컬 히스토리** (git과 별개라서 가장 가능성이 높아요)
   - VS Code: 파일 우클릭 → Timeline, 또는 `Cmd+Shift+P` → "Local History: Find Entry to Restore"
   - JetBrains: 프로젝트 우클릭 → Local History → Show History

3. **Time Machine이나 iCloud 백업**이 켜져 있다면 거기서 파일을 찾아보세요.

4. **지금은 새 작업을 하지 마세요.** 같은 파일에 덮어쓰면 복구가 더 어려워져요.

저는 지금 git 저장소가 아닌 폴더에 있어서, 프로젝트 경로를 알려 주시면 `git fsck`를 대신 돌려 드릴 수 있어요. 어떤 에디터를 쓰시는지도 알려 주세요.
