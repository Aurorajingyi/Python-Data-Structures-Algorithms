from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []
class State:
    def __init__(self, node, path_weight):
        self.node = node
        self.path_weight = path_weight
def levelOrderTraversal(root,edge_weights):
    if root is None:
        return
    q = deque()
    q.append(State(root,0)) # 根节点权重是0

    while q:
        cur_state = q.popleft()
        cur_node = cur_state.node
        cur_weight = cur_state.path_weight

        print(f"cur_node_val:{cur_node.val}, cur_node_weight:{cur_weight}")

        for child in cur_node.children:
            # 获取当前节点到child节点的权重
            edge_weight = edge_weights.get((cur_node.val, child.val), 1)
            new_weight = cur_weight + edge_weight
            q.append(State(child, new_weight))

if __name__ == "__main__":
    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)

    root.children = [node2, node3]
    node2.children = [node4, node5]

    # 每条树枝的权重：
    edge_weights = {
        (1, 2): 3,
        (1, 3): 2,
        (2, 4): 4,
        (2, 5): 1
    }
    print("层序遍历结果")
    levelOrderTraversal(root, edge_weights)


