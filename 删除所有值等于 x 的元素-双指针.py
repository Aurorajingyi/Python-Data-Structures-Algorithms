"""
给定一个顺序存储的线性表（数组形式），删除所有值等于 x 的元素，返回删除后的表。
要求：不能开辟新数组，在原数组上操作。
"""

class SequenceList():
    def __init__(self,max_size = 100):
        self.max_size = max_size
        self.length = 0
        self.data=[None]*self.max_size

    def load_data(self,data_list):
        n = len(data_list)
        if n>self.max_size:
            raise ValueError("超出最大容量")
        for i in range(n):
            self.data[i]=data_list[i]
        self.length = n
    def delete_element(self,value):
        """双指针写法，一个读、一个写，互不干扰"""
        j = 0 # 用这个索引（指针）去写
        for i in range(self.length):
            if self.data[i]!=value:
                self.data[j] = self.data[i]
                j+=1
        for k in range(j,self.length):
            self.data[k]=None
        self.length = j

    def display(self):
        print("+--" * self.length+"+")
        print("|"+"|".join([f"{str(x):2}" if x is not None else" " for x in self.data[:self.length]])+"|")
        """
        self.data[:self.length] 是切片操作，表示：
        从 self.data[0] 开始，
         一直到（但不包括）self.data[self.length]
        """
        print("+--" * self.length + "+")

# 测试
s = SequenceList()
s.load_data([-2,11,-4,13,-5,-2])
s.delete_element(-2)
s.display()