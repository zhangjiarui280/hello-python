# 生成测试日志 app.log（统一四字段：日期 时间 级别 消息）
lines = [
    "2026-11-01 10:01:00 INFO service start",
    "2026-11-01 10:02:00 ERROR db timeout",
    "2026-11-01 10:02:30 INFO retry ok",
    "2026-11-01 10:05:00 ERROR disk usage 98%",
    "2026-11-01 10:06:00 WARN memory high",
    "2026-11-01 10:07:00 INFO service stop",
]

with open("app.log", "w", encoding="utf-8") as f:
    for line in lines:
        f.write(line + "\n")

print("app.log 已生成，共", len(lines), "行")
