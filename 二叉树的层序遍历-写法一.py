from collections import deque
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
def levelOrderTraversal(root):
    if root is None:
        return

    q = deque() # 初始化队列
    q.append(root) # 将根节点加入队列

    while q: # 当队列不为空时，继续遍历
        cur = q.popleft() # 取出当前节点（队列是先进先出）
        # 访问当前节点
        print(cur.val,end=" ") # 打印当前节点的值

        # 如果当前节点有左子节点，加入队列
        if cur.left is not None:
            q.append(cur.left)

        # 如果当前节点有右子节点，加入队列
        if cur.right is not None:
            q.append(cur.right)

# 测试案例
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    levelOrderTraversal(root)



