import json                        # 引入 json 工具箱

FILE = "todos.json"                # 数据文件名（全大写表示常量，不打算改）


def load():                        # 定义函数：读文件
    try:                           # 试着执行下面这段（可能会报错）
        with open(FILE, "r", encoding="utf-8") as f:      # 打开文件：只读、utf-8 编码、起名 f
            return json.load(f)    # 把文件内容读成 Python 对象，交出去
    except FileNotFoundError:      # 如果 open 报"文件不存在"
        return []                  # 就返回空列表


def save():                        # 定义函数：写文件
    with open(FILE, "w", encoding="utf-8") as f:          # 打开文件：写模式（会清空原内容）
        json.dump(todos, f, ensure_ascii=False, indent=2) # 把 todos 写进去：中文不转义、缩进 2 格


todos = load()                     # 程序启动：先读一次文件，结果装进 todos


def show():                        # 定义函数：显示全部
    if not todos:                  # 如果 todos 是空的
        print("（还没有待办）")     # 打印提示
        return                     # 提前结束函数
    for i, t in enumerate(todos, 1):   # 遍历：i 是序号(从 1 开始)，t 是元素
        if t["done"]:              # 如果这条已完成
            mark = "x"             # 标记打 x
        else:                      # 否则
            mark = " "             # 标记是空格
        print(f"{i} [{mark}] {t['text']}")   # 打印：序号 [标记] 内容


def add(text):                     # 定义函数：添加一条，需要参数 text
    todos.append({"text": text, "done": False})   # 造新字典追加到末尾，默认未完成
    save()                         # 立刻存盘
    print(f"已添加：{text}")        # 提示


def done(i):                       # 定义函数：把第 i 条标为完成
    if 1 <= i <= len(todos):       # 序号在合法范围（1 到长度）
        todos[i - 1]["done"] = True      # 下标要减 1，把 done 改成 True
        save()                     # 立刻存盘
        print(f"已完成：{todos[i - 1]['text']}")   # 提示
    else:                          # 序号不合法
        print("序号不存在")         # 提示


def del_todo(i):                   # 定义函数：删除第 i 条
    if 1 <= i <= len(todos):       # 序号合法
        t = todos.pop(i - 1)       # 删掉并拿到被删的那个
        save()                     # 立刻存盘
        print(f"已删除：{t['text']}")   # 提示
    else:                          # 序号不合法
        print("序号不存在")         # 提示


show()                             # 调用：显示全部
print("-" * 20)                    # 打印 20 个减号当分隔线
add("学 Python")                   # 调用：添加一条
done(1)                            # 调用：把第 1 条标完成
print("-" * 20)                    # 分隔线
show()                             # 再显示一次
