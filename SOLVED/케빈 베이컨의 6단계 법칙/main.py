import sys
from collections import deque, defaultdict

def main():
    n_user, n_given = map(int, sys.stdin.readline().split())
    n_graph = n_user + 1
    graph = defaultdict(list)

    for i in range(n_given):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    
    def bfs(curr, visited):
        q = deque([curr])
        visited[curr] = 1
        while q:
            x = q.popleft()
            for y in graph[x]:
                if not visited[y]:
                    visited[y] = visited[x] + 1
                    q.append(y)
    
    answer = []
    for row in range(1, n_graph):
        visited = [0] * n_graph
        bfs(row, visited)
        answer.append(sum(visited))
    print(answer.index(min(answer)) + 1)

if __name__ == "__main__":
    main()