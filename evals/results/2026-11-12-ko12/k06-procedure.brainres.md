<!-- Q: 깃에서 실수로 main 브랜치에 바로 커밋했어. 이 커밋을 새 브랜치로 옮기려면 어떻게 해? -->

새 브랜치를 만들고, main을 원격 상태로 되돌리면 돼요. 아직 push 전이라고 가정한 방법이에요.

1. 현재 커밋을 가리키는 새 브랜치를 만들어요. (체크아웃은 안 해요.)
   ```
   git branch my-feature
   ```
2. main을 원격 main 위치로 되돌려요.
   ```
   git reset --hard origin/main
   ```
3. 새 브랜치로 이동해요.
   ```
   git switch my-feature
   ```

`reset --hard`는 커밋하지 않은 변경도 지워요. 작업 중인 파일이 있으면 먼저 `git stash`로 보관하세요. 커밋은 1번에서 `my-feature`가 이미 가리키고 있어서 사라지지 않아요.

이미 `git push`까지 했다면 다르게 해야 해요. 원격 main이 바뀐 상태라 `reset --hard`만으로는 원격이 안 돌아와요. 팀이 이미 pull했을 수 있어서, 이때는 `git revert`를 권해요. 어느 쪽인지 알려주시면 그 경우에 맞는 명령을 드릴게요.

참고로 지금 작업 폴더(`/private/var/folders/.../tmpz9eisjbg`)는 git 저장소가 아니에요. 실제 저장소 폴더로 이동한 뒤 명령을 실행하세요.
