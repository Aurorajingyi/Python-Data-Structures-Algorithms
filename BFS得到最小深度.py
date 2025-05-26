from collections import deque
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        q = deque([root])
        depth = 1 # root本身就是一层
        while q:
            size= len(q)
            for i in range(size):
                cur = q.popleft()

            # 判断是否到达叶子节点
            if cur.left is None and cur.right is None:
                return depth

            # 将下一层节点加到队列
            if cur.left is not None:
                q.append(cur.left)

            if cur.right is not None:
                q.append(cur.right)

            # 增加深度
            depth += 1
        return depth
# 测试
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    solution = Solution()
    minDepth = solution.minDepth(root)
    print(f"min depth is {minDepth}")