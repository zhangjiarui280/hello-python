# 日志分析：用 .get() 计数 + 按数量排序（写法二，最终版）
counts = {}

with open("app.log", "r", encoding="utf-8") as f:
    for line in f:
        parts = line.split(" ", 3)
        level = parts[2]
        counts[level] = counts.get(level, 0) + 1

items = sorted(counts.items(), key=lambda x: x[1], reverse=True)

for level, num in items:
    print(f"{level:<6}{num}")
