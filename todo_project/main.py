# 只负责一件事：读命令行参数，决定调用谁
import sys

from storage import load, save
from models import Todo
from actions import show_all, add, done, del_todo


def main():
    # 1. 读盘：列表 -> 对象
    todos = [Todo.from_dict(d) for d in load()]

    # 2. 没有命令，默认显示
    if len(sys.argv) < 2:
        show_all(todos)
        return

    cmd = sys.argv[1]

    # 3. 分发
    if cmd == "add":
        if len(sys.argv) < 3:
            print("用法：python main.py add 内容")
            return
        add(todos, sys.argv[2])
        print(f"已添加：{sys.argv[2]}")

    elif cmd == "list":
        show_all(todos)

    elif cmd == "done":
        if len(sys.argv) < 3:
            print("用法：python main.py done 序号")
            return
        if done(todos, int(sys.argv[2])):
            print("已标记完成")
        else:
            print("序号不存在")

    elif cmd == "del":
        if len(sys.argv) < 3:
            print("用法：python main.py del 序号")
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

    # 4. 存盘：对象 -> 列表 -> 字典
    save(todos)


if __name__ == "__main__":
    main()
