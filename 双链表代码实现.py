class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:
    def __init__(self):
        # 虚拟头尾节点（双链表）
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    # 增
    def add_last(self, val):
        x = Node(val)
        temp = self.tail.prev
        temp.next = x
        x.prev = temp
        # temp <-> x
        self.tail.prev = x
        x.next = self.tail
        # temp <-> x <-> tail
        self.size += 1

    def add_first(self, val):
        x = Node(val)
        temp = self.head.next
        # head <-> temp
        x.next = temp
        temp.prev = x
        self.head.next = x
        x.prev = self.head
        self.size += 1

    # 按索引添加
    def add(self, index, element):
        # 先判断索引是否合法
        self.check_element_index(index)
        if index == self.size:
            self.add_last(element)
            return

        # 找到index对应的Node
        p = self.get_node(index)
        # temp <-> x <-> p
        temp = p.prev
        x = Node(element)
        temp.next = x
        x.prev = temp

        p.prev = x
        x.next = p

        self.size += 1

    ##### 删
    def remove_first(self):
        if self.size < 1:
            raise IndexError("No element to remove")
        x = self.head.next # x是要删除的元素
        temp = x.next

        # head <-> x <-> temp
        # head <-> temp
        self.head.next = temp
        temp.prev = self.head

        self.size -= 1
        return x.val

    def remove_last(self):
        if self.size < 1:
            raise IndexError("No element to remove")
        x = self.tail.prev  # x 是要删除的元素
        temp = x.prev
        temp.next = self.tail
        self.tail.prev = temp

        self.size -= 1
        return x.val

    # 根据索引删除
    def remove(self, index):
        self.check_element_index(index)
        # 找到x对应的Node
        x = self.get_node(index)
        prev = x.prev
        next = x.next
        # prev <-> x <-> next
        prev.next = next
        next.prev = prev
        self.size -= 1
        return x.val

    #### 查
    def get(self, index):
        self.check_element_index(index)
        x = self.get_node(index)
        return x.val

    def get_first(self):
        if self.size < 1:
            raise IndexError("No element in the list")
        return self.head.next.val

    def get_last(self):
        if self.size < 1:
            raise IndexError("No element in the list")

    #### 改
    def set(self, index, value):
        self.check_element_index(index)
        x = self.get_node(index)
        old_val = x.val
        x.val = value
        return old_val



    #### 其他函数工具
    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def check_element_index(self, index):
        if not 0 <= index < self.size:
            raise IndexError(f"Index {index} ,size:{self.size}")

    def check_position_index(self, index):
        if not 0 <= index <= self.size:
            raise IndexError(f"Index {index}, size:{self.size}")

    def get_node(self, index):  # 获取索引节点
        self.check_element_index(index)
        p = self.head.next  # self.head 是虚拟头节点，所以p指向第一个节点
        for _ in range(index):
            p = p.next
        return p

    def display(self):
        print(f"size = {self.size}")
        p = self.head.next
        while p != self.tail:
            print(f"{p.val} <->", end="")
            p = p.next
        print("null\n")

if __name__=="__main__":
    list = MyLinkedList()
    list.add_last(1)
    list.add_last(2)
    list.add_last(3)
    list.add_first(0)
    list.add(2,100)
    list.display()
