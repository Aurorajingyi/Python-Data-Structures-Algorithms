from collections import deque

# 定义树节点类

# 定义树节点类
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 定义State类，记录节点的路径权重和
class State:
    def __init__(self, node, path_weight):
        self.node = node  # 节点
        self.path_weight = path_weight  # 节点的路径权重和


def levelOrderTraversal(root, edge_weights):
    if root is None:
        return

    q = deque()  # 初始化队列
    # 初始状态，根节点的路径权重和为 0
    q.append(State(root, 0))
    while q:  # 当这个列表不为空的时候
        # size = len(q)  # 获取这个列表的长度，即一层的节点数
        # while size > 0:
        cur_state = q.popleft()  # 取出一个节点
        cur_node = cur_state.node  # val\leftnode\rightnode
        cur_weight = cur_state.path_weight  # 当前节点的累积权重和（后面要计算）

        # 输出节点的值和累积权重和
        print(f"Node = {cur_node.val}, path_weight = {cur_weight}")
        # size -= 1

        if cur_state.node.left is not None:
            left_weigh = cur_weight + edge_weights.get((cur_node.val, cur_node.left.val), 1)
            q.append(State(cur_node.left, left_weigh))  # State: 节点、节点的路径权重和

        if cur_state.node.right is not None:
            right_weigh = cur_weight + edge_weights.get((cur_node.val, cur_node.right.val), 1)
            q.append(State(cur_node.right, right_weigh))


if __name__ == '__main__':
    # 构建一个二叉树
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # 每条树枝的权重如下：
    edge_weights = {
        (1, 2): 3,
        (1, 3): 2,
        (2, 4): 4,
        (2, 5): 1
    }
    # 调用层序遍历函数
    levelOrderTraversal(root, edge_weights)
