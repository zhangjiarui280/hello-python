# 日志分析：用 if/else 计数（写法一）
counts = {}

with open("app.log", "r", encoding="utf-8") as f:
    for line in f:
        parts = line.split(" ", 3)
        level = parts[2]
        if level in counts:
            counts[level] = counts[level] + 1
        else:
            counts[level] = 1

for level, num in counts.items():
    print(level, num)
