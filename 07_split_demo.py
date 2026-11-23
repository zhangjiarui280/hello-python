# split 练习：把一行日志拆成四段
line = "2026-11-01 10:23:45 ERROR db connection timeout"
parts = line.split(" ", 3)
print(parts)
print(f"日期：{parts[0]}")
print(f"时间：{parts[1]}")
print(f"级别：{parts[2]}")
print(f"消息：{parts[3]}")
