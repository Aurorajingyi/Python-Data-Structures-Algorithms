class Stack:
    def __init__(self):
        self.stack = [] # 用空列表保存元素

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)
        print(f"元素{item}已入栈")

    def pop(self):
        if self.is_empty():
            raise IndexError("弹出失败：栈为空")
        return self.stack.pop()

    def top(self):
        # 返回栈顶元素（不删除）
        if self.is_empty():
            raise IndexError("错误：栈为空")
        return self.stack[-1]

    def size(self):
        return len(self.stack)

# 测试
if __name__ == "__main__":
    stack = Stack() # 创建
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("当前栈顶元素", stack.top()) # 3
    stack.pop() # 出栈，弹出3
    print("当前栈顶元素", stack.top()) # 2
    print("栈大小", stack.size()) # 2