from collections import deque


# State 类：用来存储节点和路径权重
class State:
    def __init__(self, node, path_weight):
        self.node = node
        self.path_weight = path_weight


def bfs(graph, s):  # 从节点s开始遍历
    q = deque()
    q.append(State(s, 0))
    visited = [False] * len(graph)
    visited[s] = True

    while q:
        cur_state = q.popleft()
        cur_node = cur_state.node
        cur_weight = cur_state.path_weight

        # 打印当前访问的节点和路径权重
        print(f"cur_node: {cur_node}, cur_weight: {cur_weight}")

        for neighbor, edge_weight in graph[cur_node]:
            if visited[neighbor]:
                continue
            new_weight = cur_weight + edge_weight
            q.append(State(neighbor, new_weight)) # 将邻居和更新后的权重加入q队列

            visited[neighbor] = True
            print(f"  Add node {neighbor} to the queue with updated distance {new_weight}")

    # 打印从起点 s 到每个节点的最终访问状态。
    print("\nFinal distances from node", s)

    for i in range(len(graph)):
        print(f"Distance from {s} to {i}: {visited[i]}")

# 测试用例
if __name__ == "__main__":
    # 定义一个加权图：邻接表表示
    graph = {
        0: [(1, 3), (2, 2)],  # 节点0到节点1权重是3，到节点2权重是2
        1: [(0, 3), (3, 4)],  # 节点1到节点0权重是3，到节点3权重是4
        2: [(0, 2), (3, 1)],  # 节点2到节点0权重是2，到节点3权重是1
        3: [(1, 4), (2, 1)]  # 节点3到节点1权重是4，到节点2权重是1
    }

    # 从节点0开始BFS遍历
    bfs(graph, 0)