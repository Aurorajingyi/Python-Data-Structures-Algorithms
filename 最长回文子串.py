class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        # 遍历每一个字符，作为回文串的中心
        for i in range(len(s)):
            print(f"\n检查以 s[{i}] 为中心的回文串：")

            # 以 s[i] 为中心的最长回文子串
            s1 = self.palindrome(s, i, i)
            print(f"以单字符为中心，得到回文串 s1: '{s1}'")

            # 以 s[i] 和 s[i+1] 为中心的最长回文子串
            s2 = self.palindrome(s, i, i + 1)
            print(f"以双字符为中心，得到回文串 s2: '{s2}'")

            # 更新最长回文子串
            if len(s1) > len(res):
                res = s1
                print(f"当前最长回文子串更新为: '{res}'")
            if len(s2) > len(res):
                res = s2
                print(f"当前最长回文子串更新为: '{res}'")

        return res

    def palindrome(self, s: str, l: int, r: int) -> str:
        # 防止索引越界
        while l >= 0 and r < len(s) and s[l] == s[r]:
            # 向两边展开
            print(f"字符 '{s[l]}' 和 '{s[r]}' 相等，继续展开")
            l -= 1
            r += 1

        # 展开结束时的回文串
        print(f"展开结束，回文串为 s[{l + 1}:{r}] -> '{s[l + 1:r]}'")
        return s[l + 1:r]

s = "babad"
solution = Solution()
print(solution.longestPalindrome(s))
