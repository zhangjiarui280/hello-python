# 只负责一件事：对一堆待办做操作
from models import Todo


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
