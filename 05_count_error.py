# 统计 app.log 里 ERROR 的行数，输出 2
# 等价于命令：grep -c ERROR app.log
count = 0

with open("app.log", "r", encoding="utf-8") as f:
    for line in f:
        if "ERROR" in line:
            count = count + 1

print(count)
