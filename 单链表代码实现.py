class MyLinkedList2:
    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None
    """
    在该实现中，tail 并不是虚拟节点，而是链表中的实际最后一个节点。
    它直接指向链表的最后一个元素，并在每次 add_last 和 remove_last 操作时更新。
    这种设计没有使用虚拟尾节点，而是将 tail 作为最后一个有效节点的指针。
    因此，每次删除最后一个节点时，需要正确更新 tail。
    """
    def __init__(self):
        self.head = self.Node(None)  # 由于Node在这里写成内部定义，需要用self访问
        self.tail = self.Node(None)
        self.size = 0

    def add_first(self, e):
        new_node = self.Node(e)

        new_node.next = self.head.next
        self.head.next = new_node
        if self.size == 0:
            self.tail = new_node # 要制定尾指向哪里
        self.size += 1
    def add_last(self, e):
        new_node = self.Node(e)
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def add(self, index, element):
        self.check_element_index(index)
        if index == self.size:
            self.add_last(element)
            return
        p = self.get_node(index)
        new_node = self.Node(element)
        new_node.next = p.next # 顺序不能变
        p.next = new_node
        self.size += 1

    #### 删
    def remove_first(self):
        if self.is_empty():
            raise Exception("Empty list")
        first_node = self.head.next
        self.head.next = first_node.next
        # 处理特殊情况
        if self.size == 1:
            self.tail = self.head # 删除first_node,size==0
        self.size -= 1
        return first_node.val

    def remove_last(self):
        if self.is_empty():
            raise Exception("Empty list")
        last_node = self.head
        while last_node != self.tail: # 使用 last_node 遍历链表，直到找到倒数第二个节点（即 last_node.next == self.tail）。
            last_node = last_node.next
        val = self.tail.val
        last_node.next = None
        self.tail = last_node
        self.size -= 1
        return val

    def remove(self, index):
        self.check_element_index(index)
        p = self.head.next
        for _ in range(index):
            p = p.next
        need_to_remove = p.next
        p.next = need_to_remove.next
        # 删除的是最后一个元素
        if index == self.size-1:
            self.tail = p
        self.size -= 1
        return need_to_remove.val

    #### 查
    def get_first(self):
        if self.is_empty():
            raise Exception("Empty list")
        return self.head.next.val

    def get_last(self):
        if self.is_empty():
            raise Exception("Empty list")
        return self.tail.val

    def get(self, index):
        self.check_element_index(index)
        p = self.get_node(index)
        return p.val

    #### 改

    def set(self, index, element):
        self.check_element_index(index)
        p = self.get_node(index)
        old_val = p.val
        p.val = element
        return old_val

    #### 其他工具函数
    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def is_element_index(self, index):
        return 0 <= index < self.size

    def is_position_index(self, index):
        return 0 <= index <= self.size

    # 检查 index 索引位置是否可以存在元素
    def check_element_index(self, index):
        if not self.is_element_index(index):
            raise IndexError(f"Index: {index}, Size: {self.size}")

    # 检查 index 索引位置是否可以添加元素
    def check_position_index(self, index):
        if not self.is_position_index(index):
            raise IndexError(f"Index: {index}, Size: {self.size}")

    def get_node(self, index):
        p = self.head.next
        for _ in range(index):
            p = p.next
        return p

if __name__ == '__main__':
    list = MyLinkedList2()
    list.add_first(1)
    list.add_first(2)
    list.add_last(3)
    list.add_last(4)
    list.add(2, 5)

    print(list.remove_first())  # 2
    print(list.remove_last())  # 4
    print(list.remove(1))  # 5

    print(list.get_first())  # 1
    print(list.get_last())  # 3
    print(list.get(1))  # 3