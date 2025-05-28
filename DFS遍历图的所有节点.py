# 图的邻接列表表示
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        # 添加有向边 u -> v
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def neighbors(self, u):
        # 返回 u 节点的所有邻居
        return self.graph.get(u, [])


# 遍历图的所有节点
def traverse(graph, s, visited):
    # 基本情况：节点越界或者已经访问过
    if s < 0 or s >= len(graph.graph) or visited[s]:
        return

    # 前序位置：访问当前节点
    visited[s] = True
    print(f"visit {s}")

    # 遍历当前节点的所有邻居
    for neighbor in graph.neighbors(s):
        traverse(graph, neighbor, visited)

    # 后序位置：当前节点的所有邻居都已访问
    # 这里不做任何操作，但如果需要，可以在此进行其他处理
    # print(f"Backtracking from node {s}")


# 测试案例
if __name__ == "__main__":
    # 创建图实例
    g = Graph()

    # 根据提供的邻接表添加边
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 0)
    g.add_edge(1, 3)
    g.add_edge(2, 0)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    g.add_edge(4, 3)

    # 初始化访问记录数组
    visited = [False] * len(g.graph)

    # 从节点 0 开始遍历
    print("Starting DFS from node 0...")
    traverse(g, 0, visited)
