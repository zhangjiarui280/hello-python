class Todo:
    def __init__(self, text):
        self.text = text
        self.done = False

    def show(self):
        if self.done:
            mark = "x"
        else:
            mark = " "
        print(f"[{mark}] {self.text}")

    def toggle(self):
        self.done = not self.done

    def who(self):
        print("self 是：", self)


t1 = Todo("买牛奶")
t2 = Todo("写代码")

t1.show()
t2.show()

print("--- 把 t1 标记完成 ---")
t1.toggle()
t1.show()
t2.show()

print("--- 验证 self 到底是谁 ---")
t1.who()
print("t1   是：", t1)
