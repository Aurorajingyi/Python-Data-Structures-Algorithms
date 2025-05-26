class MyLinkedHashMap:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None
            self.prev = None

    def __init__(self):
        # 哈希表+双向链表
        self.head = self.Node(None, None)
        self.tail = self.Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = dict()  # 哈希表

    def get(self, key):  # 根据键获得值
        if key not in self.map:
            return None
        return self.map[key].value

    def put(self, key, value):
        if key not in self.map:
            # 在双向链表中插入新的None
            node = self.Node(key, value)  # 创建新的节点
            self.add_last_node(node)
            self.map[key] = node
            # 哈希表中存的是整个链表节点对象，而不仅仅是值。
            # 哈希表：key -> Node对象（里面有key、value、prev、next）
            return
        # 若存在，则直接替换之前的val
        self.map[key].value = value

    def add_last_node(self, x):
        temp = self.tail.prev
        x.next = self.tail
        x.prev = temp  # 习惯是先走x的前后指针
        temp.next = x
        self.tail.prev = x

    def remove(self, key):
        # 若 key 本不存在，直接返回
        if key not in self.map:
            return
        # 若 key 存在，则需要同时在哈希表和链表中删除
        node = self.map[key]  # key -> Node对象（里面有key、value、prev、next）
        del self.map[key]  # 在哈希表中删除
        self.remove_node(node)

    def remove_node(self, x):
        prev = x.prev
        next = x.next
        prev.next = next
        next.prev = prev
        x.next = x.prev = None

    def contains_keys(self, key):
        return key in self.map

    def keys(self):
        key_list = []
        p = self.head.next
        while p != self.tail:
            key_list.append(p.key)
            p = p.next
        return key_list


if __name__ == '__main__':
    map = MyLinkedHashMap()
    map.put("a", 1)
    map.put("b", 2)
    map.put("c", 3)
    map.put("d", 4)
    map.put("e", 5)  # 这是字典，字典的key是唯一的标识，value是值
    print(map.keys())
    map.remove("c")
    print(map.keys())
