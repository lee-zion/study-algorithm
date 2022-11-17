import sys
from collections import defaultdict, deque

def main():
    n = int(sys.stdin.readline())
    graph = defaultdict(list)
    for i in range(n-1):
        [x, y] = map(int, sys.stdin.readline().split(" "))
        graph[x].append(y)
        graph[y].append(x)
    visited = [0] * (n+1)
    def bfs(curr, graph, visited):
        q = deque([curr])
        visited[curr] = curr
        while q:
            v = q.popleft()
            for adj in graph[v]:
                if not visited[adj]:
                    visited[adj] = v
                    q.append(adj)
    bfs(1, graph, visited)
    for i in range(2, n+1):
        print(visited[i])

if __name__ == "__main__":
    main()