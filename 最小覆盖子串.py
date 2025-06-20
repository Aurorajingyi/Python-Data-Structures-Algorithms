class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, window = {}, {}
        # 初始化字符需求字典
        for c in t:
            need[c] = need.get(c, 0) + 1

        left = 0
        right = 0
        valid = 0
        # 记录最小覆盖子串的起始索引及长度
        start = 0
        length = float('inf')

        while right < len(s):
            # c 是将移入窗口的字符
            c = s[right]
            print(f"右指针移动到 {right}, 当前字符是 '{c}'")

            # 扩大窗口
            right += 1

            # 进行窗口内数据的一系列更新
            if c in need:
                window[c] = window.get(c, 0) + 1
                print(f"当前窗口：{window}")

                # 如果当前字符的数量满足需求
                if window[c] == need[c]:
                    valid += 1
                    print(f"字符 '{c}' 满足需求, valid 增加为 {valid}")

            # 判断左侧窗口是否要收缩
            while valid == len(need):
                print(f"窗口满足条件，准备收缩窗口，当前窗口：{window}")

                # 更新最小覆盖子串
                if right - left < length:
                    start = left
                    length = right - left
                    print(f"更新最小覆盖子串：start = {start}, length = {length}, 子串 = '{s[start:start + length]}'")

                # d 是将移出窗口的字符
                d = s[left]
                print(f"左指针移到 {left}, 当前字符是 '{d}'")

                # 缩小窗口
                left += 1

                # 进行窗口内数据的一系列更新
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                        print(f"字符 '{d}' 不再满足需求, valid 减少为 {valid}")
                    window[d] -= 1
                    print(f"更新窗口：{window}")

        # 返回最小覆盖子串
        print(f"最终最小覆盖子串起始位置 {start}, 长度 {length}")
        return "" if length == float('inf') else s[start: start + length]

s = "BANCADOBECODE"
t = "ABC"
sol = Solution()
print(sol.minWindow(s, t))
