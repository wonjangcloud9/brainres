<!-- Q: 폴더 안에 있는 이미지 파일들 이름을 날짜순으로 바꿔주는 스크립트 짜줘. -->


<invoke name="Write">
<parameter name="file_path">/private/var/folders/5v/r7qdd9b90t91plfwnfk5hdqm0000gn/T/tmpv_doczul/rename_images.py</parameter>
<parameter name="content">#!/usr/bin/env python3
"""폴더 안의 이미지 파일을 날짜순으로 정렬해 순번 이름으로 바꿉니다.

날짜 기준: EXIF 촬영일(Pillow 설치 시) -> 없으면 파일 수정 시간.

사용 예:
  python3 rename_images.py ~/Pictures/trip              # 미리보기만 (dry-run)
  python3 rename_images.py ~/Pictures/trip --apply      # 실제 변경
  python3 rename_images.py ~/Pictures/trip --apply --prefix trip_ --date-in-name
"""
import argparse
import sys
import uuid
from datetime import datetime
from pathlib import Path

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif",
              ".webp", ".heic", ".heif"}


def exif_datetime(path: Path):
    """EXIF DateTimeOriginal을 읽어 datetime으로 반환. 실패 시 None."""
    try:
        from PIL import Image
    except ImportError:
        return None
    try:
        with Image.open(path) as img:
            exif = img.getexif()
            # 0x9003 = DateTimeOriginal (Exif IFD), 0x0132 = DateTime
            value = exif.get_ifd(0x8769).get(0x9003) or exif.get(0x0132)
        if value:
            return datetime.strptime(str(value), "%Y:%m:%d %H:%M:%S")
    except Exception:
        pass
    return None


def file_datetime(path: Path) -> datetime:
    return exif_datetime(path) or datetime.fromtimestamp(path.stat().st_mtime)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("folder", type=Path, help="이미지가 있는 폴더")
    p.add_argument("--prefix", default="", help="새 이름 앞에 붙일 문자열")
    p.add_argument("--start", type=int, default=1, help="시작 번호 (기본 1)")
    p.add_argument("--date-in-name", action="store_true",
                   help="이름에 날짜(YYYYMMDD_HHMMSS)도 포함")
    p.add_argument("--apply", action="store_true",
                   help="실제로 이름 변경 (없으면 미리보기만)")
    args = p.parse_args()

    folder = args.folder.expanduser()
    if not folder.is_dir():
        print(f"폴더를 찾을 수 없습니다: {folder}", file=sys.stderr)
        return 1

    files = [f for f in folder.iterdir()
             if f.is_file() and not f.name.startswith(".")
             and f.suffix.lower() in IMAGE_EXTS]
    if not files:
        print("이미지 파일이 없습니다.")
        return 0

    dated = sorted(((file_datetime(f), f) for f in files),
                   key=lambda x: (x[0], x[1].name))
    width = max(3, len(str(args.start + len(dated) - 1)))

    plan = []
    for i, (dt, f) in enumerate(dated, start=args.start):
        parts = [args.prefix + str(i).zfill(width)]
        if args.date_in_name:
            parts.append(dt.strftime("%Y%m%d_%H%M%S"))
        new = f.with_name("_".join(parts) + f.suffix.lower())
        plan.append((f, new))

    for old, new in plan:
        print(f"{old.name}  ->  {new.name}")

    if not args.apply:
        print("\n미리보기입니다. 실제로 변경하려면 --apply 를 추가하세요.")
        return 0

    # 대상 이름이 목록 밖의 기존 파일과 겹치면 중단
    sources = {old for old, _ in plan}
    for _, new in plan:
        if new.exists() and new not in sources:
            print(f"충돌: {new.name} 이(가) 이미 존재합니다. 중단합니다.",
                  file=sys.stderr)
            return 1

    # 2단계 변경: 임시 이름 -> 최종 이름 (이름이 서로 겹쳐도 안전)
    token = uuid.uuid4().hex
    temps = []
    for old, new in plan:
        tmp = old.with_name(f".{token}_{old.name}")
        old.rename(tmp)
        temps.append((tmp, new))
    for tmp, new in temps:
        tmp.rename(new)

    print(f"\n{len(plan)}개 파일 이름을 변경했습니다.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
</parameter>
</invoke>
øf
