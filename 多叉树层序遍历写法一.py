from collections import deque
class TreeNode:
    def __init__(self, val = 0):
        self.val = val
        self.children = []

# 层序遍历方法
def level_order_traverse(root):
    if root is None:
        return

    q = deque()
    q.append(root)

    while q:
        cur = q.popleft()
        print(cur.val, end=" ") # 访问当前节点的值并输出

        # 把 cur 所有子节点加入队列
        for child in cur.children:
            q.append(child)
# 测试
root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

# 组装
root.children = [node2, node3, node4]
node2.children = [node5, node6]
node3.children = [node7]

# 调用层序遍历
print("层序遍历结果：")
level_order_traverse(root)
