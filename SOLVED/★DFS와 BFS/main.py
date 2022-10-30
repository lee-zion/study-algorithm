import sys
from collections import defaultdict, deque

def get_adj_list(g_raw, FROM_INDEX_ZERO = True, IS_BIDIR = True):
    graph = defaultdict(list)
    for g in g_raw:
        [depart, dest] = map(int, g.split(" "))
        if FROM_INDEX_ZERO:
            graph[depart-1].append(dest-1)
            if IS_BIDIR:
                graph[dest-1].append(depart-1)
        else:
            graph[depart].append(dest)
            if IS_BIDIR:
                graph[dest].append(depart)
    for g in graph.keys():
        graph[g].sort()
    return graph

def main():
    [N, M, V] = map(int, sys.stdin.readline().split(" "))
    graph = []
    for i in range(M):
        graph.append(sys.stdin.readline().strip())
    graph = get_adj_list(graph)

    def dfs(current, graph, visited, FROM_INDEX_ZERO = True):
        nonlocal answer
        visited[current] = True
        if FROM_INDEX_ZERO:
            answer.append(current+1)
        else:
            answer.append(current)

        if isinstance(graph, defaultdict):
            # graph == adj_list
            for adj in graph[current]:
                if not visited[adj]:
                    dfs(adj, graph, visited)
        elif isinstance(graph, list):
            # graph == adj_matrix
            for adj, is_connected in enumerate(graph[current]):
                if is_connected and not visited[adj]:
                    dfs(adj, graph, visited)
    
    def bfs(current, graph, visited, FROM_INDEX_ZERO = True):
        nonlocal answer
        q = deque([current])
        visited[current] = True
        if FROM_INDEX_ZERO:
            answer.append(current+1)
        else:
            answer.append(current)

        while q:
            current = q.popleft()
            if isinstance(graph, defaultdict):
                # graph == adj_list
                for adj in graph[current]:
                    if not visited[adj]:
                        q.append(adj)
                        visited[adj] = True
                        if FROM_INDEX_ZERO:
                            answer.append(adj+1)
                        else:
                            answer.append(adj)
            elif isinstance(graph, list):
                # graph == adj_matrix
                for adj, is_connected in enumerate(graph[current]):
                    if is_connected and not visited[adj]:
                        q.append(adj)
                        visited[adj] = True
                        if FROM_INDEX_ZERO:
                            answer.append(adj+1)
                        else:
                            answer.append(adj)
    
    answer, visited = [], [False] * N
    dfs(V-1, graph, visited)
    print(" ".join(map(str, answer)))
    answer, visited = [], [False] * N
    bfs(V-1, graph, visited)
    print(" ".join(map(str, answer)))


if __name__ == "__main__":
    main()