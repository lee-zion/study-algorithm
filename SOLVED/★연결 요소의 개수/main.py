import sys
from collections import defaultdict, deque

def bfs(current, graph, visited):
    q = deque([])
    visited[current] = True
    q.append(current)
    while q:
        v = q.popleft()
        for adj in graph[v]:
            if not visited[adj]:
                visited[adj] = True
                q.append(adj)

def main():
    [N, M] = map(int, sys.stdin.readline().split(" "))
    graph = defaultdict(list)
    for i in range(M):
        [u, v] = map(int, sys.stdin.readline().split(" "))
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    for key in graph.keys():
        graph[key].sort()
    
    visited = [False] * N
    answer = 0

    while not all(visited):
        for i, is_visited in enumerate(visited):
            if not is_visited:
                answer += 1
                bfs(i, graph, visited)
    print(answer)

if __name__ == "__main__":
    main()