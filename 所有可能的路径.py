from typing import List


class Solution:
    # 记录所有路径
    def __init__(self):
        self.res = []
        self.path = []

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # 启动从节点0开始的深度优先搜索
        print(f"Starting traversal from node 0.")
        self.traverse(graph, 0)

        print(f"All paths found: {self.res}")
        return self.res

    # 图的遍历框架
    def traverse(self, graph: List[List[int]], s: int):
        # 添加节点 s 到路径
        print(f"Visiting node {s}, current path: {self.path}")
        self.path.append(s)

        n = len(graph)
        # 如果到达终点节点
        if s == n - 1:
            print(f"Reached the target node {s}, path: {self.path}")
            self.res.append(self.path.copy())
            self.path.pop()  # 回溯，移除最后一个节点
            return

        # 递归访问相邻节点
        for v in graph[s]:
            print(f"Node {s} can go to {v}. Recursively visiting.")
            self.traverse(graph, v)

        # 从路径移出节点 s
        print(f"Backtracking from node {s}, current path before popping: {self.path}")
        self.path.pop()


# 测试用例
graph = [[1, 2], [3], [3], []]

solution = Solution()
result = solution.allPathsSourceTarget(graph)
print("Final result:", result)
