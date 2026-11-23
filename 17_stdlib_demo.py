from pathlib import Path
from datetime import datetime

folder = Path("_test_org")

print("=== 1. 基本 ===")
print("路径：", folder)
print("绝对路径：", folder.resolve())
print("存在吗：", folder.exists())
print("是目录吗：", folder.is_dir())

print()
print("=== 2. 遍历目录 ===")
for f in folder.iterdir():
    print("  ", f.name)

print()
print("=== 3. 文件信息 ===")
for f in folder.iterdir():
    if f.is_file():
        size = f.stat().st_size
        mtime = datetime.fromtimestamp(f.stat().st_mtime)
        print(f"  {f.name:<10} {f.suffix:<6} {size:>5} 字节   {mtime:%Y-%m-%d %H:%M}")

print()
print("=== 4. 筛选：只要 txt ===")
txts = [f for f in folder.iterdir() if f.suffix == ".txt"]
print("  ", [f.name for f in txts])

print()
print("=== 5. 拼路径 + 新建目录 ===")
target = folder / "子目录" / "a.txt"
print("  拼出来的路径：", target)
target.parent.mkdir(parents=True, exist_ok=True)
target.write_text("hello", encoding="utf-8")
print("  写入成功：", target.exists())
print("  读回来：", target.read_text(encoding="utf-8"))

print()
print("=== 6. datetime ===")
now = datetime.now()
print("  现在：", now)
print("  格式化：", now.strftime("%Y年%m月%d日 %H:%M"))
print("  指定日期：", datetime(2026, 12, 12, 19, 30))
d1 = datetime(2026, 11, 23)
d2 = datetime(2026, 12, 12)
print("  相差：", (d2 - d1).days, "天")
