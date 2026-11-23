# 待办清单 v1（内存版）：增、查、标完成、删
todos = [
    {"text": "买牛奶", "done": False},
    {"text": "写代码", "done": True},
    {"text": "跑步", "done": False},
]


def show():
    for i, t in enumerate(todos, 1):
        if t["done"]:
            mark = "x"
        else:
            mark = " "
        print(f"{i} [{mark}] {t['text']}")


def add(text):
    todos.append({"text": text, "done": False})
    print(f"已添加：{text}")


def done(i):
    todos[i - 1]["done"] = True
    print(f"已完成：{todos[i - 1]['text']}")


def del_todo(i):
    t = todos.pop(i - 1)
    print(f"已删除：{t['text']}")


show()
print("-" * 20)
add("学 Python")
done(1)
del_todo(2)
print("-" * 20)
show()
