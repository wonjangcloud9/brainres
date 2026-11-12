<!-- Q: 내일 아침에 발표인데 슬라이드 파일이 날아갔어. 어떡해? -->

먼저 이 Mac에서 복구 가능한 흔적이 있는지 찾아볼게요. 읽기 전용 검색만 합니다.


<invoke name="Bash">
<parameter name="command">find ~ -xdev \( -iname "*.pptx" -o -iname "*.ppt" -o -iname "*.key" -o -iname "*.odp" -o -iname "*.pdf" \) -mtime -30 -not -path "*/Library/Caches/*" -not -path "*/node_modules/*" 2>/dev/null | head -50</parameter>
<parameter name="description">Find recently modified slide/PDF files in home</parameter>
</invoke>
<parameter name="Bash">
<parameter name="command">ls -la ~/.Trash 2>&1 | head -40; echo ---; ls -la ~/Library/Containers/com.microsoft.Powerpoint/Data/Library/Preferences/AutoRecovery 2>&1 | head; echo ---; ls -la ~/Library/Containers/com.apple.iWork.Keynote/Data/Library 2>&1 | head; echo ---; tmutil listlocalsnapshots / 2>&1 | head</parameter>
<parameter name="description">Check Trash, Office/Keynote autosave dirs, and local snapshots</parameter>
</invoke>



<invoke name="Bash">
<parameter name="command">mdfind -onlyin ~ 'kMDItemContentTypeTree == "public.presentation"' 2>/dev/null | head -30</parameter>
<parameter name="description">Spotlight search for presentation files</parameter>
</invoke>
