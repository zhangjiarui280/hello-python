# ============================================================
# v1 - v3 自测题
#
# 怎么用：
#   1. 每题下面有一个【答题区】，在答题区里写你的代码
#   2. 把 pass 删掉，写你的实现（写多少行都行）
#   3. 保存，运行这个文件
#   4. 拉到最下面看得分
#
# 规则：不查笔记，可以查文档。每题都必须能跑通。
# =================.....................................................................................===========================================

import json
import sys

FILE = "自测_todos.json"
todos = []


def save():
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)


# ############################################################
# 第一档 · 函数题（每题 8 分）
# ############################################################


# ------------------------------------------------------------
# 题 1 · count_done
#
# 要求：返回已完成的条数
# 例子：count_done([{"text":"a","done":True},{"text":"b","done":False}]) -> 1
# 提示：需要一个计数器，遍历列表，判断 t["done"]
# ------------------------------------------------------------
def count_done(items):
      # ========== 答题区（在下面写） ==========
   s=0
   for i,t in enumerate(items):
       if t["done"]:
           s=s+1
   return s


    # ========== 答题区结束 ==========


# ------------------------------------------------------------
# 题 2 · search
#
# 要求：返回所有 text 里包含 keyword 的条目，组成【新列表】
#       原来的 items 不能被修改
# 例子：search([{"text":"买牛奶"},{"text":"买面包"}], "牛奶") -> 只有牛奶那条
# 提示：先建空列表 result，遍历时把符合条件的 append 进去，最后 return
# ------------------------------------------------------------
def search(items, keyword):
    # ========== 答题区（在下面写） ==========

    pass

    # ========== 答题区结束 ==========


# ------------------------------------------------------------
# 题 3 · sort_by_done
#
# 要求：返回新列表，未完成的在前，已完成的在后
#       同一组里保持原来的先后顺序
# 例子：sort_by_done([完成, 未完成, 未完成]) -> [未完成, 未完成, 完成]
# 提示：sorted(items, key=lambda t: t["done"])
#       False 排 True 前面，正好是你要的顺序
# ------------------------------------------------------------
def sort_by_done(items):
    # ========== 答题区（在下面写） ==========

    pass

    # ========== 答题区结束 ==========


# ############################################################
# 第二档 · 改错题（每题 10 分）
#
# 这三个函数已经有代码了，但都有 bug。
# 直接在答题区里改，不用重写整个文件。
# ############################################################


# ------------------------------------------------------------
# 题 4 · add
#
# 现象：加完一条，关掉程序再打开，数据没了
# 要求：改完以后，add 完能从 json 文件里读到这条
# ------------------------------------------------------------
def add(text):
    # ========== 答题区（在这里改） ==========

    todos.append({"text": text, "done": False})
    print(f"已添加：{text}")

    # ========== 答题区结束 ==========


# ------------------------------------------------------------
# 题 5 · load
#
# 现象：第一次运行（还没有 json 文件）直接崩溃
# 要求：文件不存在时返回空列表 []
# ------------------------------------------------------------
def load():
    # ========== 答题区（在这里改） ==========

    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)

    # ========== 答题区结束 ==========


# ------------------------------------------------------------
# 题 6 · main
#
# 现象：敲 python t.py 崩溃；敲 python t.py add 也崩溃
# 要求：两种情况都不能崩，都要打印一句提示
#       - 没有命令        -> 打印提示
#       - 有 add 但没内容  -> 打印提示
# ------------------------------------------------------------
def main():
    # ========== 答题区（在这里改） ==========

    cmd = sys.argv[1]
    if cmd == "add":
        add(sys.argv[2])

    # ========== 答题区结束 ==========


# ############################################################
# 第三档 · 扩展题（每题 12 分）
# ############################################################


# ------------------------------------------------------------
# 题 7 · clear
#
# 要求：清空所有待办（原地清空这个列表，不要新建列表）
# 例子：data = [{"text":"a"}]; clear(data); data == []
# 提示：列表有一个方法能原地清空
# ------------------------------------------------------------
def clear(items):
    # ========== 答题区（在下面写） ==========

    pass

    # ========== 答题区结束 ==========


# ------------------------------------------------------------
# 题 8 · edit
#
# 要求：把第 i 条（从 1 开始）的 text 改成 new_text
#       成功返回 True，序号不存在返回 False
# 例子：edit([{"text":"a"}], 1, "新内容") -> True
#       edit([{"text":"a"}], 99, "x")     -> False
# 提示：先判断 1 <= i <= len(items)，再改 items[i-1]["text"]
# ------------------------------------------------------------
def edit(items, i, new_text):
    # ========== 答题区（在下面写） ==========

    pass

    # ========== 答题区结束 ==========


# ------------------------------------------------------------
# 题 9 · count
#
# 要求：返回字符串，格式必须是：共 X 条，已完成 Y 条
# 例子：count([完成, 未完成, 完成]) -> "共 3 条，已完成 2 条"
# 提示：len(items) 是总数，可以调用上面的 count_done(items)
#       注意 f-string 里的中文和空格，一个字都不能差
# ------------------------------------------------------------
def count(items):
    # ========== 答题区（在下面写） ==========

    pass

    # ========== 答题区结束 ==========


# ############################################################
# 第四档 · 综合题（10 分）
# ############################################################


# ------------------------------------------------------------
# 题 10 · show_with_priority
#
# 要求：把每条待办打印出来，要显示优先级
#   新数据：{"text":"a","done":False,"priority":"高"}  -> 显示"高"
#   老数据：{"text":"b","done":True}                   -> 显示"中"，不能崩
# 输出示例（格式随意，每行有文字和优先级即可）：
#   [ ] a  高
#   [x] b  中
# 提示：t.get("priority", "中")  —— 有就用，没有就给默认值
# ------------------------------------------------------------
def show_with_priority(items):
    # ========== 答题区（在下面写） ==========

    pass

    # ========== 答题区结束 ==========


# ############################################################
# 下面是自动批改，不要改
# ############################################################

results = []


def check(label, points, fn):
    try:
        ok = fn()
    except Exception as e:
        results.append((label, False, points, str(e)[:40]))
        return
    results.append((label, bool(ok), points, ""))


def t1():
    return count_done([{"text": "a", "done": True},
                       {"text": "b", "done": False},
                       {"text": "c", "done": True}]) == 2


def t2():
    data = [{"text": "买牛奶", "done": False}, {"text": "买面包", "done": True}]
    r = search(data, "牛奶")
    return len(r) == 1 and r[0]["text"] == "买牛奶" and len(data) == 2


def t3():
    r = sort_by_done([{"text": "a", "done": True},
                      {"text": "b", "done": False},
                      {"text": "c", "done": False}])
    return [x["text"] for x in r] == ["b", "c", "a"]


def t4():
    global todos
    import os
    todos = []
    if os.path.exists(FILE):
        os.remove(FILE)
    add("测试项")
    with open(FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return len(data) == 1


def t5():
    import os
    if os.path.exists(FILE):
        os.remove(FILE)
    return load() == []


def t6():
    import io
    import contextlib
    old = sys.argv
    try:
        for args in (["t.py"], ["t.py", "add"]):
            sys.argv = args
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                main()
            if not buf.getvalue().strip():
                sys.argv = old
                return False
    except Exception:
        sys.argv = old
        return False
    sys.argv = old
    return True


def t7():
    data = [{"text": "a"}, {"text": "b"}]
    clear(data)
    return data == []


def t8():
    data = [{"text": "a"}, {"text": "b"}]
    ok = edit(data, 1, "新内容")
    bad = edit(data, 99, "x")
    return ok is True and bad is False and data[0]["text"] == "新内容"


def t9():
    return count([{"text": "a", "done": True},
                  {"text": "b", "done": False},
                  {"text": "c", "done": True}]) == "共 3 条，已完成 2 条"


def t10():
    import io
    import contextlib
    items = [{"text": "新", "done": False, "priority": "高"},
             {"text": "老", "done": True}]
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        show_with_priority(items)
    out = buf.getvalue()
    return ("高" in out) and ("中" in out)


check("题 1  count_done", 8, t1)
check("题 2  search", 8, t2)
check("题 3  sort_by_done", 8, t3)
check("题 4  add 存盘", 10, t4)
check("题 5  load 不崩", 10, t5)
check("题 6  main 不崩", 10, t6)
check("题 7  clear", 12, t7)
check("题 8  edit", 12, t8)
check("题 9  count", 12, t9)
check("题 10 兼容老数据", 10, t10)

print()
print("=" * 46)
total = 0
got = 0
for label, ok, pts, err in results:
    total += pts
    if ok:
        got += pts
        print("  [通过] " + label + "  +" + str(pts))
    else:
        print("  [未过] " + label + ("   (" + err + ")" if err else ""))
print("=" * 46)
print("得分：" + str(got) + " / " + str(total))
print()
if got >= 90:
    print("完全掌握。可以进面向对象了。")
elif got >= 75:
    print("大部分会了。把没过的那几题补掉。")
elif got >= 60:
    print("能跟着写，独立会卡。重做一遍 v2 和 v3。")
else:
    print("还没长在手上。从头手写一遍。")
