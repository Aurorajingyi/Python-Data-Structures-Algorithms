"""
给定一个顺序存储的线性表（数组形式），删除所有值等于 x 的元素，返回删除后的表。
要求：不能开辟新数组，在原数组上操作。
"""
class SequenceList:
    def __init__(self,max_size = 100):
        self.max_size = max_size
        self.length = 0
        self.data = [None] * self.max_size

    def load_data(self,data_list):
        """加载一组数据，并同步更新length"""
        n = len(data_list)
        if n>self.max_size:
            raise ValueError("超出最大容量")
        for i in range(n):
            self.data[i] = data_list[i]
        self.length = n

    """方法一：倒序遍历"""
    def delete_element(self,value):
        for i in range(self.length-1,-1,-1): # 倒序删除
            if self.data[i] == value:
                # 用数组模拟线性表
                for j in range(i,self.length -1):
                    self.data[j] = self.data[j+1] # 用self.data[i+1]覆盖掉self.data[i]
                self.data[self.length-1] = None # 最后一个位置为None
                self.length -= 1

    def display(self):
        print("+--"* self.length + "+")
        print("|"+"|".join([f"{str(x):2}" if x is not None else " " for x in self.data[:self.length]])+"|")
        print("+--"*self.length+"+")
# 测试
s = SequenceList()
s.load_data([-2,11,-4,13,-5,-2])
s.delete_element(-2)
s.display()
