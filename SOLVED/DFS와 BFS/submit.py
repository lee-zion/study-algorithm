import sys
from collections import defaultdict, deque

def get_adj_list(g_raw):
    graph = defaultdict(list)
    for g in g_raw:
        [depart, dest] = map(int, g.split(" "))
        graph[dest-1].append(depart-1)
        graph[depart-1].append(dest-1)
    for g in graph.keys():
        graph[g].sort()
    return graph

def main():
    [N, M, V] = map(int, sys.stdin.readline().split(" "))
    graph = []
    for i in range(M):
        graph.append(sys.stdin.readline().strip())
    graph = get_adj_list(graph)

    def dfs(current, graph, visited):
        nonlocal answer
        visited[current] = True
        answer.append(current+1)
        for adj in graph[current]:
            if not visited[adj]:
                dfs(adj, graph, visited)
    
    def bfs(current, graph, visited):
        nonlocal answer
        q = deque([current])
        visited[current] = True
        answer.append(current+1)
        while q:
            current = q.popleft()
            for adj in graph[current]:
                if not visited[adj]:
                    q.append(adj)
                    visited[adj] = True
                    answer.append(adj+1)
    
    answer, visited = [], [False] * N
    dfs(V-1, graph, visited)
    print(" ".join(map(str, answer)))
    answer, visited = [], [False] * N
    bfs(V-1, graph, visited)
    print(" ".join(map(str, answer)))


if __name__ == "__main__":
    main()