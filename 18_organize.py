from pathlib import Path


def organize(folder_name):
    folder = Path(folder_name)

    if not folder.is_dir():
        print("不是文件夹：", folder)
        return

    count = 0
    for f in list(folder.iterdir()):
        if not f.is_file():
            continue

        ext = f.suffix.lstrip(".") or "无后缀"
        target_dir = folder / ext
        target_dir.mkdir(exist_ok=True)

        f.rename(target_dir / f.name)
        print(f"  {f.name:<12} -> {ext}/")
        count += 1

    print(f"共整理 {count} 个文件")


if __name__ == "__main__":
    organize("_test_org")
