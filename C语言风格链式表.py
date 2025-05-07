class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None  # 空链表初始化，头指针为空

    def length(self):
        """求链表长度"""
        p = self.head
        j = 0
        while p:
            p = p.next
            j += 1
        return j

    def find_kth(self, k):
        """查找第k个节点（k从1开始）"""
        p = self.head
        i = 1
        while p and i < k:
            p = p.next
            i += 1
        if i == k:
            return p
        else:
            return None

    def find(self, x):
        """查找第一个值为x的节点"""
        p = self.head
        while p and p.data != x:
            p = p.next
        return p

    def insert(self, x, i):
        """在第i-1个节点后插入新节点，i从1开始"""
        new_node = Node(x)
        if i == 1:
            # 插到表头
            new_node.next = self.head
            self.head = new_node
            return True
        else:
            p = self.find_kth(i - 1)
            if not p:
                print(f"插入失败：第{i-1}个节点不存在")
                return False
            new_node.next = p.next
            p.next = new_node
            return True

    def delete(self, i):
        """删除第i个节点，i从1开始"""
        if i == 1:
            if not self.head:
                return False
            s = self.head
            self.head = self.head.next
            del s
            return True
        else:
            p = self.find_kth(i - 1)
            if not p or not p.next:
                print(f"删除失败：第{i}个节点不存在")
                return False
            s = p.next
            p.next = s.next
            del s
            return True

    def display(self):
        """打印链表内容"""
        p = self.head
        elements = []
        while p:
            elements.append(str(p.data))
            p = p.next
        print(" -> ".join(elements) if elements else "空链表")

if __name__ == "__main__":
    llist = LinkedList()

    print("\n--- 测试插入 ---")
    llist.insert(10, 1)
    llist.insert(20, 2)
    llist.insert(15, 2)  # 插入到中间
    llist.insert(30, 4)  # 插到末尾
    llist.display()

    print("\n链表长度：", llist.length())

    print("\n查找第2个元素：", llist.find_kth(2).data if llist.find_kth(2) else "未找到")
    print("查找值为15的节点：", llist.find(15).data if llist.find(15) else "未找到")

    print("\n--- 测试删除 ---")
    llist.delete(2)  # 删除中间元素
    llist.display()
    llist.delete(1)  # 删除头部元素
    llist.display()
    llist.delete(2)  # 删除尾部元素
    llist.display()
