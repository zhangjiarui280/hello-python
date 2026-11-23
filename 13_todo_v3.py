# 待办清单 v3：命令行版
# 用法：
#   python 13_todo_v3.py                显示全部
#   python 13_todo_v3.py add 买牛奶      添加一条
#   python 13_todo_v3.py list           显示全部
#   python 13_todo_v3.py done 1         把第 1 条标完成
#   python 13_todo_v3.py del 2          删除第 2 条

import sys
import json

FILE = "todos.json"


# ---------- 第一段：读和写 ----------

def load():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save():
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)


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
    save()
    print(f"已添加：{text}")


def done(i):
    if 1 <= i <= len(todos):
        todos[i - 1]["done"] = True
        save()
        print(f"已完成：{todos[i - 1]['text']}")
    else:
        print("序号不存在")


def del_todo(i):
    if 1 <= i <= len(todos):
        t = todos.pop(i - 1)
        save()
        print(f"已删除：{t['text']}")
    else:
        print("序号不存在")


# ---------- 第三段：新的部分 ----------
# 根据命令行参数，决定调用哪个函数

def main():
    # 一个参数都没带 → 默认显示列表
    if len(sys.argv) < 2:
        show()
        return

    cmd = sys.argv[1]          # 第一个参数：命令

    if cmd == "add":
        if len(sys.argv) < 3:  # 缺内容
            print("用法：python 13_todo_v3.py add 内容")
            return
        add(sys.argv[2])

    elif cmd == "list":
        show()

    elif cmd == "done":
        if len(sys.argv) < 3:
            print("用法：python 13_todo_v3.py done 序号")
            return
        done(int(sys.argv[2]))

    elif cmd == "del":
        if len(sys.argv) < 3:
            print("用法：python 13_todo_v3.py del 序号")
            return
        del_todo(int(sys.argv[2]))

    else:
        print("未知命令：", cmd)
        print("可用命令：add / list / done / del")


main()
