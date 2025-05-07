class SequenceList:
    def __init__(self, max_size=10):
        """初始化顺序表，默认最大容量为10"""
        self.max_size = max_size
        self.length = 0
        self.data = [None] * self.max_size

    def is_empty(self):
        """判断是否为空"""
        return self.length == 0

    def is_full(self):
        """判断是否已满"""
        return self.length == self.max_size

    def get_element(self, index):
        """获取指定位置的元素（索引从0开始）"""
        if 0 <= index < self.length:  # 修复了原来条件的错误，应该是 index 在 [0, length) 范围内
            return self.data[index]
        else:
            return IndexError("Index out of range")

    def locate_element(self, value):
        """查找元素值=value的首次出现的索引，找不到返回-1"""
        for i in range(self.length):
            if self.data[i] == value:
                return i
        return -1

    def insert_element(self, index, value):
        """在指定位置插入元素（返回操作是否成功）"""
        if self.is_full():
            print("顺序已满，插入失败")
            return False
        if index < 0 or index > self.length:  # 允许插入到表尾！
            print("插入位置不合法")
            return False
        # 将索引位置即之后元素往后移
        for i in range(self.length - 1, index - 1, -1):
            self.data[i + 1] = self.data[i]

        self.data[index] = value
        self.length += 1
        return True

    def delete_element(self, index):
        """删除指定位置的元素（返回操作是否成功）"""
        if index < 0 or index >= self.length:
            print("删除位置不合法")
            return False
        # 往前移
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        self.length -= 1
        self.data[self.length] = None  # 清空被删除元素的位置
        return True

    def display(self):
        """打印当前顺序表内容"""
        print("+--" * self.max_size + "+")
        print("|" + "|".join([f"{str(x):2}" if x is not None else " " for x in self.data]) + "|")
        print("+--" * self.max_size + "+")
        print(f"当前长度：{self.length}/{self.max_size}")


# 测试
if __name__ == "__main__":
    seq_list = SequenceList(max_size=5)

    print("\n--- 测试插入操作 ---")
    seq_list.insert_element(0, 10)
    seq_list.insert_element(1, 20)
    seq_list.insert_element(1, 15)  # 中间插入
    seq_list.insert_element(3, 30)  # 尾插
    seq_list.display()

    print("\n元素 15 的索引位置:", seq_list.locate_element(15))
    print("\n索引 2 的元素值：", seq_list.get_element(2))

    print("\n--- 测试删除操作 ---")
    seq_list.delete_element(1)  # 删除中间元素
    seq_list.display()
    seq_list.delete_element(0)  # 删除头部元素
    seq_list.display()
    seq_list.delete_element(2)  # 删除尾部元素
    seq_list.display()  # 不合法

    print("\n--- 测试边界条件 ---")
    seq_list.display()
    print("尝试插入到非法位置：", seq_list.insert_element(5, 50)) # 此时的length是2，所以不符合插入条件

