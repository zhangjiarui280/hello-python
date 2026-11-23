# 演示 1：类变量 vs 实例变量
class A:
    count = 0          # 类变量：所有对象共享一份

    def __init__(self, name):
        self.name = name

    def inc_wrong(self):
        self.count += 1    # 陷阱：会在对象身上新建一个 count


class B:
    count = 0

    def __init__(self, name):
        self.name = name

    def inc_right(self):
        B.count += 1       # 正确：改的是类上的那个 count


a1 = A("一")
a2 = A("二")
a1.inc_wrong()
a1.inc_wrong()
print("=== 错误写法 self.count += 1 ===")
print("A.count =", A.count)
print("a1.count =", a1.count)
print("a2.count =", a2.count)

b1 = B("一")
b2 = B("二")
b1.inc_right()
b2.inc_right()
b2.inc_right()
print()
print("=== 正确写法 B.count += 1 ===")
print("B.count =", B.count)
print("b1.count =", b1.count)
print("b2.count =", b2.count)


# 演示 2：继承
class Todo:
    def __init__(self, text):
        self.text = text
        self.done = False

    def show(self):
        mark = "x" if self.done else " "
        print(f"[{mark}] {self.text}")

    def toggle(self):
        self.done = not self.done


class TimedTodo(Todo):
    def __init__(self, text, deadline):
        super().__init__(text)
        self.deadline = deadline

    def show(self):
        super().show()
        print(f"      截止：{self.deadline}")

    def is_overdue(self, today):
        return today > self.deadline


print()
print("=== 继承 ===")
t = TimedTodo("交作业", "2026-11-20")
t.show()
t.toggle()
t.show()
print("过期了吗：", t.is_overdue("2026-11-10"))
print("isinstance(t, Todo)      =", isinstance(t, Todo))
print("isinstance(t, TimedTodo) =", isinstance(t, TimedTodo))

print()
print("=== 父类的方法，子类自动拥有 ===")
plain = Todo("普通待办")
plain.toggle()
plain.show()
