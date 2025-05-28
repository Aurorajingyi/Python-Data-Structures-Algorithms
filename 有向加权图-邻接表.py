from collections import defaultdict


# 加权有向图的通用实现（邻接表）
class WeightedDigraph:
    # 存储相邻节点及边的权重
    class Edge:
        def __init__(self, to: int, weight: int):
            self.to = to  # 相邻节点
            self.weight = weight

    # WeightedDigraph 类的初始化方法 __init__
    def __init__(self, n: int):  # n代表节点数（后面用）
        self.graph = defaultdict(list)  # 用defaultdict来初始化一个空列表

    # 增: 添加一条带权重的有向边，复杂度O(1)
    def addEdge(self, from_: int, to: int, weight: int):  # from不能作为变量名，from_
        self.graph[from_].append(self.Edge(to, weight))  # Edge:存储相邻节点及边的权重

    # 删：删除一条有向边，复杂度O(1)
    def removeEdge(self, from_: int, to: int):
        self.graph[from_] = [e for e in self.graph[from_] if e.to != to]

    """
    遍历 self.graph[from_] 中的所有边 e
    只有 e.to != to 的边会被保留下来，表示排除了从 from_ 到 to 的边。
    self.graph[from_] 得到的是 节点 from_ 的所有邻接边.
    """

    # 查：判断两个节点是否相邻，复杂度O(v)
    def hasEdge(self, from_: int, to: int) -> bool:  # 返回bool: True/False
        return any(e.to == to for e in self.graph[from_])

    # 查：返回一条边的权重，复杂度O(v)
    def weight(self, from_: int, to: int) -> int:
        edge = next((e for e in self.graph[from_] if e.to == to), None)
        if edge is None:
            raise ValueError
        return edge.weight

    # 查：查询某个节点的所有邻居节点，复杂度O(1)
    def neighbors(self, v: int):  # v代表图中的某个节点，会返回这个节点的所有邻居节点）。
        return self.graph[v]

    """
    v 在 neighbors(v) 方法中与 from_ 在 addEdge(from_, to, weight) 方法中是一样的
    """


if __name__ == '__main__':
    graph = WeightedDigraph(3)  # 图中节点数：3
    graph.addEdge(0, 1, 1)
    graph.addEdge(1, 2, 2)
    graph.addEdge(2, 0, 3)
    graph.addEdge(2, 1, 4)

    print(graph.hasEdge(0, 1))  # True
    print(graph.hasEdge(1, 0))  # False

    print(graph.weight(1, 2))  # 2
    """
    graph.neighbors(2) 返回的是节点 2 的所有邻居，
    它会返回一个 边的列表，而不是单一的数字。
    
    print(graph.neighbors(2))  
    graph.removeEdge(2, 0)
    print(graph.neighbors(2))  #
    """

    # 打印节点2的所有邻居节点
    print([edge.to for edge in graph.neighbors(2)])

    # 删除从节点2到0的边
    graph.removeEdge(2, 0)

    # 打印节点2的所有邻居节点
    print([edge.to for edge in graph.neighbors(2)])
