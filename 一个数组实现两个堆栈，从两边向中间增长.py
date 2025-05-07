# 定义最大容量
MaxSize = 10

# 双栈类
class DoubleStack:
    def __init__(self):
        self.data = [None] * MaxSize
        self.Top1 = -1 # 栈1从左边增长
        self.Top2 = MaxSize # 栈2从右边向左边增长

    def push(self, item, tag):
         """入栈操作，tag=1表示第一个栈，tag=2表示第二个栈"""
         if self.Top2 - self.Top1 == 1:
             print("堆栈满")
             return
         if tag == 1:
             self.Top1 += 1
             self.data[self.Top1] = item
         elif tag == 2:
             self.Top2 -= 1
             self.data[self.Top2] = item
         else:
             raise ValueError("错误，tag必须是1或者2")

    def pop(self,tag):
        """出栈操作，tag=1表示第一个栈，tag=2表示第二个栈"""
        if tag == 1:
            if self.Top1 == -1:
                print("栈1空")
                return None # 如果为空用return提前退出
            item = self.data[self.Top1]
            self.Top1 -= 1
            return item
        if tag == 2:
            if self.Top2 == MaxSize:
                print("栈2空")
                return None
            item = self.data[self.Top2]
            self.Top2 +=1
            return item
        else:
            raise ValueError("错误，tag必须是1或者2")

    def is_empty(self,tag):
        if tag == 1:
            return self.Top1 == -1
        elif tag == 2:
            return self.Top2 == MaxSize
        else:
            raise ValueError("错误，tag必须是1或者2")

    def display(self):
        """一行展示当前双栈的分布"""
        display_line = ""
        for index in range(MaxSize):
            if index <= self.Top1:
                display_line += f"[{self.data[index]}]"
            elif index >= self.Top2:
                display_line += f"[{self.data[index]}]"
            else:
                display_line += "[   ]"  # 空闲区域用空格表示
        print(display_line)

# 测试代码
if __name__ == "__main__":
    ds = DoubleStack()
    ds.push(10,1)
    ds.push(10,2)
    ds.push(20,2)

    print("栈1 POP：",ds.pop(1))
    print("栈1是否为空？",ds.is_empty(1))
    print("栈2是否为空？",ds.is_empty(2))

    print("\n栈内元素分布:")
    ds.display()


