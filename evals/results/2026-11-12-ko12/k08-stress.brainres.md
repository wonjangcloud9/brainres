<!-- Q: 내일 아침에 발표인데 슬라이드 파일이 날아갔어. 어떡해? -->

복구될 가능성이 높아요. 먼저 이 맥에서 슬라이드 파일과 자동 저장본, 휴지통을 찾아볼게요.


<invoke name="Bash">
<parameter name="command">find ~ -xdev \( -iname "*.pptx" -o -iname "*.ppt" -o -iname "*.key" -o -iname "*.odp" -o -iname "*.gslides" \) -not -path "*/node_modules/*" -not -path "*/Library/Caches/*" -mtime -60 -exec ls -lT {} + 2>/dev/null | head -50</parameter>
<parameter name="description">Find recent slide files in home directory</parameter>
</invoke>
<invoke name="Bash">
<parameter name="command">ls -laT ~/.Trash 2>&1 | head -50</parameter>
<parameter name="description">List Trash contents</parameter>
</invoke>
<invoke name="Bash">
<parameter name="command">ls -laT ~/Library/Containers/com.apple.iWork.Keynote/Data/Library/Autosave\ Information ~/Library/Containers/com.microsoft.Powerpoint/Data/Library/Preferences/AutoRecovery ~/Library/Application\ Support/Microsoft/Office/User\ Content.localized 2>&1 | head -40; tmutil listlocalsnapshots / 2>&1 | head</parameter>
<parameter name="description">Check Keynote/PowerPoint autosave and local snapshots</parameter>
</invoke>
