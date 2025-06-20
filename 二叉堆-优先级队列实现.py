class MyPriorityQueue:
    def __init__(self, capacity, comparator=None):
        # 堆数组
        self.heap = [0] * capacity
        # 堆中元素的数量
        self.size = 0
        # 元素比较器
        self.comparator = comparator if comparator is not None else lambda x, y: (x > y) - (x < y)

    # 返回堆的数量
    def size(self):
        return self.size

    # 判断堆是否为空
    def is_empty(self):
        return self.size == 0

    # 父节点的索引
    def parent(self, node):
        return (node - 1) // 2

    # 左子节点的索引
    def left(self, node):
        return node * 2 + 1

    # 右子节点的索引
    def right(self, node):
        return node * 2 + 2

    # 交换数组的两个元素
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # 查：返回堆顶元素
    def peek(self):
        if self.is_empty():
            raise IndexError("empty heap")
        return self.heap[0]

    # 插：向堆中插入一个元素，时间复杂度是 O(logN)
    # 把新元素追加到最后，然后上浮到正确位置
    def push(self, x):
        # 扩容
        if self.size == len(self.heap):
            self.resize(2 * len(self.heap))
        # 把新元素加到最后
        self.heap[self.size] = x
        # 然后上浮到正确的位置
        self.swim(self.size)
        self.size += 1

    # 删：删除堆顶元素，时间复杂度为O(logN)
    def pop(self):
        if self.is_empty():
            raise IndexError("empty heap")
        # 取出栈顶元素
        res = self.heap[0]
        # 把最后一个元素移到栈顶，交换
        self.swap(0, self.size - 1)
        self.heap[self.size - 1] = None
        self.size -= 1
        # 然后下沉到正确位置
        self.sink(0)
        # 缩容
        if self.size > 0 and self.size == len(self.heap) // 4:
            self.resize(len(self.heap) // 2)

        return res

    # 上浮操作，时间复杂度是O(logN)
    # 小顶堆
    def swim(self, node):
        while node > 0 and self.comparator(self.heap[self.parent(node)], self.heap[node]) > 0:
            self.swap(node, self.parent(node))
            node = self.parent(node)

    # 下沉操作
    def sink(self, node):
        while self.left(node)<self.size: # 确保左节点存在
            # 比较自己和左右节点，看谁小
            min_node = node
            if self.left(node) < self.size and self.comparator(self.heap[self.left(node)], self.heap[min_node]) < 0:
                min_node = self.left(node)
            if self.right(node) < self.size and self.comparator(self.heap[self.right(node)], self.heap[min_node]) < 0:
                min_node = self.right(node)
            if min_node == node:
                break # 如果当前节点已经是最小的，不需要交换

            # 如果左右节点中有比自己小的，就交换
            self.swap(node, min_node)
            node = min_node

    def resize(self, capacity):
        assert capacity >= self.size  # 调试和检查错误
        new_heap = [None] * capacity
        for i in range(self.size):
            new_heap[i] = self.heap[i]
        self.heap = new_heap

# test
if __name__ == '__main__':
    # 小堆顶
    pq = MyPriorityQueue(3)
    pq.push(3)
    pq.push(1)
    pq.push(4)
    pq.push(1)
    pq.push(5)
    pq.push(9)

    # 1 1 3 4 5 9
    while not pq.is_empty():
        print(pq.pop())