from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

def level_order_traversal(root):
    if root is None:
        return
    q = deque()
    q.append(root)
    # 增加记录深度的功能
    depth = 1

    while q:
        size = len(q)
        for _ in range(size):
            cur = q.popleft()
            print(cur.val, end=' ')

            # 访问cur的下一层节点
            for child in cur.children:
                q.append(child)
        depth += 1
# 测试
if __name__ == '__main__':
    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)

    # 架构
    root.children = [node2, node3, node4]
    node2.children = [node5, node6]
    node3.children = [node7]

    # 调用
    print("层序遍历结果：")
    level_order_traversal(root)


