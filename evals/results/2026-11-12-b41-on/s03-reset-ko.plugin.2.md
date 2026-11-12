<!-- Q: 급해요 ㅠㅠ git reset --hard 해서 오늘 작업한 거 다 날아갔어요. 커밋은 안 했어요. -->

`git add`를 한 번이라도 했다면 복구할 수 있어요. 한 번도 안 했다면 git에서는 복구할 수 없고, 에디터 기록이나 백업으로 찾아야 해요.

**먼저:** `git gc`, `git prune`은 **실행하지 마세요**. 복구할 데이터가 지워질 수 있어요.

1. 작업하던 저장소에서 `git fsck --lost-found`를 실행하세요. `dangling blob` 줄이 나오면 stage했던 파일이 남아 있다는 뜻이에요.
2. `.git/lost-found/other/`에 파일이 생겨요. 이름은 해시라서 `grep -rl "찾을 코드" .git/lost-found/other/`로 내용을 찾으세요.
3. git에 없으면 에디터 기록을 보세요.
   - VS Code: 파일 선택 후 Explorer 하단의 **Timeline**
   - JetBrains: 파일 우클릭 후 **Local History → Show History**
4. 그래도 없으면 Time Machine이나 iCloud, Dropbox 같은 백업 폴더를 확인하세요.
5. 찾기 전에는 그 파일들을 새로 저장하지 마세요. 에디터 기록이 덮어써질 수 있어요.

stage하지 않은 변경은 git이 저장한 적이 없어요. 그래서 1~2번이 비어 있을 수 있어요.

저장소 경로를 알려 주시면 제가 `git fsck`를 대신 실행해서 찾아볼게요.
