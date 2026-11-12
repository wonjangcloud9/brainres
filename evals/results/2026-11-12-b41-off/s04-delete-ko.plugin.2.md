<!-- Q: 망했어... 터미널에서 실수로 프로젝트 폴더를 통째로 지웠어. 휴지통에도 없어. 맥이야. -->

**먼저 새 파일 저장과 설치를 멈추세요.** `rm`으로 지운 파일은 휴지통을 거치지 않아요. 디스크에 덮어쓰기가 일어날수록 복구 확률이 떨어져요.

아래 순서대로 확인해 보세요. 위에 있을수록 성공 확률이 높아요.

1. **Git 원격 저장소**: GitHub나 GitLab에 push한 적이 있으면 `git clone`으로 거의 다 돌아와요.
2. **Time Machine이나 로컬 스냅샷**: 터미널에서 `tmutil listlocalsnapshots /`를 실행해 보세요. 스냅샷이 보이면 Time Machine에서 복구할 수 있어요.
3. **클라우드 동기화**: iCloud Drive, Dropbox, Google Drive의 웹 휴지통을 확인하세요. 폴더가 그쪽에 있었다면 30일 정도 보관돼요.
4. **에디터 로컬 기록**: VS Code는 Timeline 확장이나 `Local History` 확장에, JetBrains는 우클릭 후 `Local History > Show History`에 남아 있을 수 있어요. 열려 있던 에디터 창은 닫지 마세요.

위 방법이 모두 안 되면 복구 소프트웨어(Disk Drill 등)가 남아요. 다만 최신 맥은 SSD에 APFS를 쓰고 TRIM이 동작해서 성공률이 낮아요. 지금 기대하지는 마세요.

폴더가 있던 경로를 알려 주세요. 예를 들어 `~/Documents/myproject`처럼요. 그러면 스냅샷과 Git 상태를 같이 확인해 볼게요.
