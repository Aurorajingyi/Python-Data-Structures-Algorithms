
class Solution:
    class ListNode:
        def __init__(self, val):
            self.val = val
            self.next = None
    # 从左向右移动的指针
    left = None
    # 从右向左移动的指针
    right = None

    # 记录链表是否为回文
    res = True

    def isPalindrome(self, head: ListNode) -> bool:
        self.left = head
        print(f"开始判断回文链表，头节点：{head.val}")  # 调试信息：开始判断
        self.traverse(head)
        return self.res

    def traverse(self, right: ListNode):
        if right is None:
            return

        # 利用递归，走到链表尾部
        self.traverse(right.next)

        # 后序遍历位置，此时的 right 指针指向链表右侧尾部
        # 所以可以和 left 指针比较，判断是否是回文链表
        print(f"当前左指针值: {self.left.val}, 当前右指针值: {right.val}")  # 调试信息：比较前

        if self.left.val != right.val:
            print(f"发现不同: 左指针 {self.left.val}, 右指针 {right.val}")  # 调试信息：不匹配
            self.res = False

        # 左指针向右移动
        self.left = self.left.next

        # 打印当前比较后，左指针已经移动
        print(f"左指针已经移动，新的左指针值: {self.left.val if self.left else 'None'}")  # 调试信息：左指针更新

# 创建链表：1 -> 2 -> 3 -> 2 -> 1
if __name__ == '__main__':
    node1 = Solution.ListNode(1)
    node2 = Solution.ListNode(2)
    node3 = Solution.ListNode(3)
    node4 = Solution.ListNode(2)
    node5 = Solution.ListNode(1)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    # 创建 Solution 对象并调用 isPalindrome 方法
    solution = Solution()
    result = solution.isPalindrome(node1)

    print(f"链表是否为回文: {result}")