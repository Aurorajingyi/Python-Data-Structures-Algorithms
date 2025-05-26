# 定义元素类型
ElementType = int


# 栈节点类
class SNode:
    def __init__(self, data: ElementType):
        self.data = data
        self.next = None  # 定义指针


# 栈类
class LinkedStack:
    def __init__(self):
        self.head = SNode(None)  # 头节点，head不存数据

    def is_empty(self):
        return self.head.next is None

    def push(self, item: ElementType):
        # 不需要判断是否满
        new_node = SNode(item)
        new_node.next = self.head.next
        self.head.next = new_node
        print(f"元素{item}已入栈")

    def pop(self):
        if self.is_empty():
            print("栈空")
            return None
        first_node = self.head.next
        self.head.next = first_node.next
        top_elem = first_node.data
        print(f"元素{top_elem}已出栈")
        return top_elem

    def top(self):
        # 返回栈顶元素（不删除）
        if self.is_empty():
            print("栈空")
            return None
        return self.head.next.data


# 测试代码
if __name__ == "__main__":
    stack = LinkedStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("当前栈顶元素：", stack.top())  # 3
    stack.pop()
    stack.pop()
    stack.pop()
    # 后进先出
    print("当前是否为空栈：", stack.is_empty())
