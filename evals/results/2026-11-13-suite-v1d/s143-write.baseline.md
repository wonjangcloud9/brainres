<!-- Q: Write a bash script that backs up a folder to a tar.gz named with today's date. -->

<invoke name="Write">
<parameter name="file_path">/private/var/folders/5v/r7qdd9b90t91plfwnfk5hdqm0000gn/T/tmp93_gz3gw/backup.sh</parameter>
<parameter name="content">#!/usr/bin/env bash
# Back up a folder to a tar.gz named with today's date.
# Usage: ./backup.sh <source_folder> [destination_dir]

set -euo pipefail

if [[ $# -lt 1 || $# -gt 2 ]]; then
    echo "Usage: $0 <source_folder> [destination_dir]" >&2
    exit 1
fi

src="${1%/}"
dest="${2:-.}"

if [[ ! -d "$src" ]]; then
    echo "Error: '$src' is not a directory." >&2
    exit 1
fi

mkdir -p "$dest"

name="$(basename "$src")"
date_str="$(date +%Y-%m-%d)"
archive="$dest/${name}_${date_str}.tar.gz"

if [[ -e "$archive" ]]; then
    echo "Error: '$archive' already exists." >&2
    exit 1
fi

tar -czf "$archive" -C "$(dirname "$src")" "$name"

echo "Backup created: $archive"
</parameter>
</invoke>
<invoke name="Bash">
<parameter name="command">chmod +x /private/var/folders/5v/r7qdd9b90t91plfwnfk5hdqm0000gn/T/tmp93_gz3gw/backup.sh</parameter>
<parameter name="description">Make backup script executable</parameter>
</invoke>
.


<invoke name="Bash">
<parameter name="command">cd /private/var/folders/5v/r7qdd9b90t91plfwnfk5hdqm0000gn/T/tmp93_gz3gw && mkdir -p /tmp/bk_test_src /tmp/bk_test_out && echo hi > /tmp/bk_test_src/a.txt && ./backup.sh /tmp/bk_test_src /tmp/bk_test_out && tar -tzf /tmp/bk_test_out/bk_test_src_2026-11-13.tar.gz && ./backup.sh /tmp/bk_test_src /tmp/bk_test_out; echo "exit: $?"; rm -rf /tmp/bk_test_src /tmp/bk_test_out</parameter>
<parameter name="description">Test backup script, then clean up temp files</parameter>
</invoke>
