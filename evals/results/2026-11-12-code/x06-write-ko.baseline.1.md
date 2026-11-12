<!-- Q: 폴더 안에 있는 이미지 파일들 이름을 날짜순으로 바꿔주는 스크립트 짜줘. -->

스크립트를 작성하겠습니다.


<invoke name="Write">
<parameter name="file_path">/private/var/folders/5v/r7qdd9b90t91plfwnfk5hdqm0000gn/T/tmpv_doczul/rename_by_date.py</parameter>
<parameter name="content">#!/usr/bin/env python3
"""폴더 안의 이미지 파일을 날짜순으로 정렬해 순번 이름(예: photo_001.jpg)으로 바꿉니다.

날짜 기준: EXIF 촬영일(Pillow 설치 시) -> 없으면 파일 수정일.
기본은 미리보기(dry-run)이며, --apply 를 붙여야 실제로 이름이 바뀝니다.

사용 예:
    python3 rename_by_date.py ~/Pictures/trip
    python3 rename_by_date.py ~/Pictures/trip --prefix trip_ --apply
"""
import argparse
import sys
import uuid
from datetime import datetime
from pathlib import Path

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif",
              ".webp", ".heic", ".heif"}


def exif_date(path: Path):
    """EXIF 촬영 시각을 반환. 없거나 Pillow가 없으면 None."""
    try:
        from PIL import Image
    except ImportError:
        return None
    try:
        with Image.open(path) as img:
            exif = img.getexif()
            # 36867: DateTimeOriginal, 306: DateTime (Exif IFD 포함)
            raw = exif.get_ifd(0x8769).get(36867) or exif.get(306)
        if raw:
            return datetime.strptime(str(raw).strip(), "%Y:%m:%d %H:%M:%S")
    except Exception:
        pass
    return None


def file_date(path: Path) -> datetime:
    return exif_date(path) or datetime.fromtimestamp(path.stat().st_mtime)


def main() -> int:
    ap = argparse.ArgumentParser(description="이미지 파일을 날짜순 번호로 이름 변경")
    ap.add_argument("folder", type=Path, help="이미지가 들어 있는 폴더")
    ap.add_argument("--prefix", default="photo_", help="새 파일명 접두사 (기본: photo_)")
    ap.add_argument("--start", type=int, default=1, help="시작 번호 (기본: 1)")
    ap.add_argument("--reverse", action="store_true", help="최신 파일이 먼저 오도록")
    ap.add_argument("--apply", action="store_true", help="실제로 이름 변경 (없으면 미리보기)")
    args = ap.parse_args()

    if not args.folder.is_dir():
        print(f"폴더를 찾을 수 없습니다: {args.folder}", file=sys.stderr)
        return 1

    files = [p for p in args.folder.iterdir()
             if p.is_file() and p.suffix.lower() in IMAGE_EXTS]
    if not files:
        print("이미지 파일이 없습니다.")
        return 0

    # 날짜 -> 기존 이름 순으로 정렬 (날짜가 같으면 결과가 항상 동일하도록)
    files.sort(key=lambda p: (file_date(p), p.name), reverse=args.reverse)

    width = max(3, len(str(args.start + len(files) - 1)))
    plan = []
    for i, src in enumerate(files, start=args.start):
        dst = src.with_name(f"{args.prefix}{i:0{width}d}{src.suffix.lower()}")
        plan.append((src, dst))

    for src, dst in plan:
        mark = "" if src.name != dst.name else "  (변경 없음)"
        print(f"{src.name}  ->  {dst.name}{mark}")

    if not args.apply:
        print(f"\n미리보기입니다. 총 {len(plan)}개. 실제로 바꾸려면 --apply 를 붙이세요.")
        return 0

    # 대상 이름이 기존 파일과 겹쳐 덮어쓰는 일을 막기 위해 2단계로 변경
    plan = [(s, d) for s, d in plan if s.name != d.name]
    source_names = {s.name for s, _ in plan}
    for _, dst in plan:
        if dst.exists() and dst.name not in source_names:
            print(f"오류: {dst.name} 이(가) 이미 존재해 중단합니다. --prefix 를 바꿔보세요.",
                  file=sys.stderr)
            return 1

    token = uuid.uuid4().hex[:8]
    temps = []
    for src, dst in plan:
        tmp = src.with_name(f".tmp_{token}_{src.name}")
        src.rename(tmp)
        temps.append((tmp, dst))
    for tmp, dst in temps:
        tmp.rename(dst)

    print(f"\n완료: {len(plan)}개 이름 변경")
    return 0


if __name__ == "__main__":
    sys.exit(main())
</parameter>
</invoke>
:
