class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def load_data(self, data_list):
        if not data_list:
            return
        # 如果是空的data_list就结束
        self.head = ListNode(data_list[0]) # 第一个元素作为head，转成ListNode结构
        cur = self.head # 用current指针遍历
        for data in data_list[1:]:
            cur.next = ListNode(data)
            cur = cur.next

    def reverse_linkedlist(self):
        # 初始化两个指针
        prev = None
        cur = self.head
        while cur is not None:
            next_lk = cur.next
            cur.next=prev # 更改方向
            prev = cur # 向右移动
            cur = next_lk # 向右移动
        self.head = prev #新的头节点，要用全局变量self.head

    def display(self):
        current = self.head
        nodes = []
        while current is not None:
            nodes.append(f"{current.data}")
            current = current.next
        print("->".join(nodes) if nodes else "Empty List")

# 测试
if __name__ == '__main__':
    l = LinkedList()
    l.load_data([1, 2, 3, 4, 5])
    l.display()
    l.reverse_linkedlist()
    l.display()






