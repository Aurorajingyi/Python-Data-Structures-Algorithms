class ListNode:
    """链表节点类"""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """链表类"""

    def __init__(self):
        self.head = None  # 定义头指针
        self.length = 0

    def is_empty(self):
        """判断链表是否为空"""
        return self.head is None

    def get_element(self, index):
        """根据索引获取链表中的节点值（索引从0开始）"""
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")
        # 循环找对应索引
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def locate_element(self, value):
        """根据value找索引"""
        current = self.head  # current作工具指针去遍历
        index = 0
        while current is not None:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1  # 未找到

    def insert(self, index, value):
        """在链表的index位置插入value"""
        if index < 0 or index > self.length:  # 允许插入到表尾(index = length)
            raise IndexError("Insert position out of range")

        new_node = ListNode(value)

        # 情况1：插入到头部（Index = 0）
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            # 情况2：在链表中插入
            prev = self.head  # 从头节点开始遍历，找到index-1的位置
            for _ in range(index - 1):
                prev = prev.next
            # 链接新节点
            new_node.next = prev.next
            prev.next = new_node

        self.length += 1
        return True

    def delete(self, index):
        """删除链表中index位置的节点"""
        if index < 0 or index >= self.length:
            raise IndexError("Delete position out of range")

        # 情况1：删除头节点
        if index == 0:
            to_delete = self.head
            self.head = self.head.next
            del to_delete  # 显式释放
        else:
            # 情况2：先找到index-1的位置
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next
            prev.next = prev.next.next  # 跳过待删除节点

        self.length -= 1
        return True

    def display(self):
        """可视化链表结构"""
        current = self.head
        nodes = []
        while current is not None:
            nodes.append(f"{current.data}")
            current = current.next
        print("->".join(nodes) if nodes else "Empty List")


# 测试
if __name__ == "__main__":
    linked_list = LinkedList()
    print("\n--- 测试插入操作 ---")
    linked_list.insert(0, 10)
    linked_list.insert(1, 20)
    linked_list.insert(1, 15)  # 中间插入
    linked_list.insert(3, 30)  # 尾部插入
    linked_list.display()

    print("\n元素20的索引值：", linked_list.locate_element(20))
    print("\n索引1的元素值：", linked_list.get_element(1))

    print("\n--- 测试删除操作 ---")
    linked_list.delete(1)  # 删除中间节点15
    linked_list.display()
