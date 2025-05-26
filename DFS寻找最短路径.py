class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.minDepthValue = float("inf")
        self.currentDepth = 0

    def traverse(self, root :TreeNode) ->None:
        if root is None:
            return

        # 前序位置进入节点时增加深度
        self.currentDepth += 1

        # 如果是叶子节点
        if root.left is None and root.right is None:
            self.minDepthValue = min(self.minDepthValue, self.currentDepth)

        self.traverse(root.left)
        self.traverse(root.right)

        # 后序位置离开节点时深度减少
        self.currentDepth -= 1

    def minDepth(self, root:TreeNode) -> int:
        if root is None:
            return 0
        # 从根节点开始DFS遍历
        self.traverse(root)
        return self.minDepthValue
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # 调用minDepth函数
    solution = Solution()
    minDepth = solution.minDepth(root)
    print(f"Min depth is {minDepth}")

