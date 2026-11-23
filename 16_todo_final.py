import sys
import json

FILE = "todos.json"


class Todo:
    def __init__(self, text, done=False):
        self.text = text
        self.done = done

    def to_dict(self):
        return {"text": self.text, "done": self.done}

    @classmethod
    def from_dict(cls, d):
        return cls(d["text"], d["done"])

    def show(self, i):
        mark = "x" if self.done else " "
        print(f"{i} [{mark}] {self.text}")


def load():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save(todos):
    data = [t.to_dict() for t in todos]
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def show_all(todos):
    if not todos:
        print("（还没有待办）")
        return
    for i, t in enumerate(todos, 1):
        t.show(i)


def add(todos, text):
    todos.append(Todo(text))


def done(todos, i):
    if 1 <= i <= len(todos):
        todos[i - 1].done = True
        return True
    return False


def del_todo(todos, i):
    if 1 <= i <= len(todos):
        todos.pop(i - 1)
        return True
    return False


def main():
    raw = load()
    todos = [Todo.from_dict(d) for d in raw]

    if len(sys.argv) < 2:
        show_all(todos)
        return

    cmd = sys.argv[1]

    if cmd == "add":
        if len(sys.argv) < 3:
            print("用法：python 16_todo_final.py add 内容")
            return
        add(todos, sys.argv[2])
        print(f"已添加：{sys.argv[2]}")

    elif cmd == "list":
        show_all(todos)

    elif cmd == "done":
        if len(sys.argv) < 3:
            print("用法：python 16_todo_final.py done 序号")
            return
        if done(todos, int(sys.argv[2])):
            print("已标记完成")
        else:
            print("序号不存在")

    elif cmd == "del":
        if len(sys.argv) < 3:
            print("用法：python 16_todo_final.py del 序号")
            return
        if del_todo(todos, int(sys.argv[2])):
            print("已删除")
        else:
            print("序号不存在")

    elif cmd == "clear":
        todos.clear()
        print("已清空")

    else:
        print("未知命令：", cmd)
        print("可用命令：add / list / done / del / clear")
        return

    save(todos)


if __name__ == "__main__":
    main()
    #测试提交
