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
    # 记录当前遍历到的层数（根节点视为第 1 层）
    depth = 1
    while q: # 当队列不为空时，继续遍历
        sz = len(q) # 获取当前队列的大小，即当前层的节点数
        while sz > 0:
            cur = q.popleft() # 取出当前节点（队列是先进先出）
            # 访问当前节点
            # 输出深度和当前层的节点值
            print(f"depth = {depth}, cur = {cur.val}")

            # 每次访问一个节点，sz减少1
            sz -= 1

            # 如果当前节点有左子节点，加入队列
            if cur.left is not None:
                q.append(cur.left)

            # 如果当前节点有右子节点，加入队列
            if cur.right is not None:
                q.append(cur.right)
        #  每遍历完一层，depth 增加 1。
        depth += 1

# 测试案例
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    levelOrderTraversal(root)



