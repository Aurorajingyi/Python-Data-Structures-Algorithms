class WeightedDigraph:
    # 存储相邻节点及边的权重
    class Edge:
        def __init__(self, to: int, weight: int):
            self.to = to
            self.weight = weight

    def __init__(self, n):
        # 初始化邻接矩阵，matrix[from][to] 存储从节点 from 到节点 to 的边的权重，0 表示没有连接
        self.matrix = [[0] * n for _ in range(n)]  # [0]*n是行，n决定列
        self.n = n  # 图的节点数

    # 增：添加一条带权重的有向边，复杂度是 O(1)
    def add_edge(self, from_node, to, weight):
        self.matrix[from_node][to] = weight

    # 删：删除一条有向边，复杂度是 O(1)
    def delete_edge(self, from_node, to):
        self.matrix[from_node][to] = 0

    # 查：判断两个节点是否相邻，复杂度是 O(1)
    def has_edge(self, from_node, to):
        return self.matrix[from_node][to] != 0

    # 查：返回一条边的权重，复杂度是 O(1)
    def weight(self, from_node, to):
        return self.matrix[from_node][to]

    # 查：返回某个节点的所有邻居节点及权重，复杂度是 O(V)
    def neighbors(self, v):
        return [self.Edge(i, self.matrix[v][i]) for i in range(self.n) if self.matrix[v][i] > 0]

if __name__ == "__main__":
    # 创建一个图，节点数为 3
    graph = WeightedDigraph(3)

    # 添加边
    graph.add_edge(0, 1, 1)
    graph.add_edge(1, 2, 2)
    graph.add_edge(2, 0, 3)
    graph.add_edge(2, 1, 4)

    # 判断是否有边
    print(graph.has_edge(0, 1))  # True
    print(graph.has_edge(0, 2))  # False

    # 获取节点 2 的所有邻居节点及权重
    print([(edge.to, edge.weight) for edge in graph.neighbors(2)])
    # 输出：[(0, 3), (1, 4)]

    # 删除从节点 2 到节点 0 的边
    graph.delete_edge(2, 0)

    # 打印节点 2 的所有邻居节点
    print([edge.to for edge in graph.neighbors(2)])  # 输出：[1]
