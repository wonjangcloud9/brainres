<!-- Q: Write a bash script that backs up a folder to a tar.gz named with today's date. -->


<invoke name="Write">
<parameter name="file_path">/private/var/folders/5v/r7qdd9b90t91plfwnfk5hdqm0000gn/T/tmp93_gz3gw/backup.sh</parameter>
<parameter name="content">#!/usr/bin/env bash
# Usage: ./backup.sh <source_folder> [destination_folder]
# Creates <destination_folder>/<folder_name>_YYYY-MM-DD.tar.gz

set -euo pipefail

if [[ $# -lt 1 || $# -gt 2 ]]; then
    echo "Usage: $0 <source_folder> [destination_folder]" >&2
    exit 1
fi

src="${1%/}"
dest="${2:-.}"

if [[ ! -d "$src" ]]; then
    echo "Error: '$src' is not a directory." >&2
    exit 1
fi

mkdir -p "$dest"

name="$(basename "$(cd "$src" && pwd)")"
date_stamp="$(date +%Y-%m-%d)"
archive="$dest/${name}_${date_stamp}.tar.gz"

# -C keeps paths inside the archive relative (no leading directories)
tar -czf "$archive" -C "$(dirname "$(cd "$src" && pwd)")" "$name"

echo "Backup created: $archive"
</parameter>
</invoke>
.
