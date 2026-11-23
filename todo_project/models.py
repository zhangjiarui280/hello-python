# 只负责一件事：定义"一条待办"长什么样

class Todo:
    def __init__(self, text, done=False):
        self.text = text
        self.done = done

    def to_dict(self):
        """对象 -> 字典（存盘前用）"""
        return {"text": self.text, "done": self.done}

    @classmethod
    def from_dict(cls, d):
        """字典 -> 对象（读盘后用）"""
        return cls(d["text"], d["done"])

    def show(self, i):
        """显示自己，i 是序号"""
        mark = "x" if self.done else " "
        print(f"{i} [{mark}] {self.text}")
