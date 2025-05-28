from collections import deque
def bfs(graph, s): # 从节点s开始
    visited = [False] * len(graph)
    q = deque()
    q.append(s)
    visited[s] = True

    # 记录从s走到当前节点的步数
    step = 0
    print(f"Starting BFS from node {s}.\n")

    while q:
        size = len(q)   # 当前层的节点数
        for i in range(size):
            cur = q.popleft()
            print(f"visit:{cur} at step{step}")
            for e in graph[cur]: # cur的邻居
                if visited[e]:
                    continue
                q.append(e)
                visited[e] = True
        step += 1

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