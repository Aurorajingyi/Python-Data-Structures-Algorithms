import random


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val


class MyArrayHashMap:
    def __init__(self):
        # 存储 key 和 key 在 arr 中的索引（删除操作）
        self.map = {}
        # 真正存储 key-value 的数组
        self.arr = []

    # 根据key得到值
    def get(self, key):
        # 字典天然就用 key 来进行查找。
        if key not in self.map:
            return None
        idx = self.map[key]
        return self.arr[idx].val

    def put(self, key, val):
        if self.containsKey(key):
            # 修改
            idx = self.map[key]
            self.arr[idx].val = val
            return
        # 新增
        self.arr.append(Node(key, val))  # 列表中每一个索引存放的是Node
        self.map[key] = len(self.arr) - 1

    def containsKey(self, key):
        return key in self.map

    def remove(self, key):
        if key not in self.map:
            return

        idx = self.map[key]
        node = self.arr[idx]

        # 1. 最后一个元素 e 和第 index 个元素 node 换位置
        e = self.arr[-1]  # 取到一个node
        self.arr[-1] = self.arr[idx]
        self.arr[idx] = e
        # 2. 修改 map 中 e.key 对应的索引
        self.map[e.key] = idx
        # 3. 在数组中删除最后一个元素
        self.arr.pop()
        # 4. 在 map 中删除 node.key
        # del self.map[node.key]
        self.map.pop(node.key)

    # 随机弹出一个键
    def randomKey(self):
        randomIndex = random.randint(0, len(self.arr) - 1)
        return self.arr[randomIndex].key

    def size(self):
        return len(self.map)


if __name__ == '__main__':
    map = MyArrayHashMap()
    map.put(1, 1)
    map.put(2, 2)
    map.put(3, 3)
    map.put(4, 4)
    map.put(5, 5)

    print(map.get(1))  # 1
    print(map.randomKey())

    map.remove(4)
    print(map.randomKey())
    print(map.randomKey())
