# ============================================================
# 待办清单 v2：把数据存进 todos.json
#
# 程序从上往下执行，分成三段：
#   第一段：两个工具 —— load() 读文件，save() 写文件
#   第二段：四个操作 —— show / add / done / del_todo
#   第三段：启动和测试
#
# 和 v1 的区别只有两点：
#   1. 数据不写死在代码里，而是从 todos.json 读出来
#   2. 每次改完，马上写回文件
# ============================================================

import json

FILE = "todos.json"


# ---------- 第一段：两个工具 ----------

def load():
    """从文件读数据。文件不存在（第一次运行）就返回空列表。"""
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save():
    """把 todos 写回文件。"""
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)


# 程序一启动，先把数据读进来
todos = load()


# ---------- 第二段：四个操作 ----------

def show():
    if not todos:
        print("（还没有待办）")
        return
    for i, t in enumerate(todos, 1):
        if t["done"]:
            mark = "x"
        else:
            mark = " "
        print(f"{i} [{mark}] {t['text']}")


def add(text):
    todos.append({"text": text, "done": False})
    save()                       # ← 改完立刻存盘
    print(f"已添加：{text}")


def done(i):
    if 1 <= i <= len(todos):
        todos[i - 1]["done"] = True
        save()                   # ← 改完立刻存盘
        print(f"已完成：{todos[i - 1]['text']}")
    else:
        print("序号不存在")


def del_todo(i):
    if 1 <= i <= len(todos):
        t = todos.pop(i - 1)
        save()                   # ← 改完立刻存盘
        print(f"已删除：{t['text']}")
    else:
        print("序号不存在")


# ---------- 第三段：测试 ----------

show()
print("-" * 20)
add("学 Python")
done(1)
print("-" * 20)
show()
