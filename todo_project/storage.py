# 只负责一件事：读写 json 文件
import json

FILE = "todos.json"


def load():
    """读文件，返回一个列表（里面是字典）。文件不存在就返回空列表。"""
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save(todos):
    """把一堆 Todo 对象写进文件。"""
    data = [t.to_dict() for t in todos]
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
