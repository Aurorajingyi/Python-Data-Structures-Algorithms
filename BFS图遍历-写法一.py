from collections import deque
def bfs(graph, s):
    visited = [False] * len(graph)
    q = deque()
    q.append(s)
    visited[s] = True

    while q:
        cur = q.popleft()  # 找q的下一层
        print(f"visit {cur}")  # 打印当前访问的节点
        for e in graph[cur]:
            if visited[e]:
                continue  # 如果改邻居已经访问过，跳过
            q.append(e)
            visited[e] = True

# 测试
if __name__ == '__main__':
    graph = [
        [1, 2],
        [0, 3],
        [0, 3],
        [1, 2]
    ]

    #  从0开始BFS遍历
    bfs(graph, 0)
