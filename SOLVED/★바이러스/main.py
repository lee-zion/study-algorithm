import sys
from collections import defaultdict, deque

def main():
    n_com = int(sys.stdin.readline())
    n_conn = int(sys.stdin.readline())
    visited = [0] * n_com
    graph = defaultdict(list)
    for i in range(n_conn):
        depart, dest = map(int, sys.stdin.readline().split(" "))
        graph[depart - 1].append(dest - 1)
        graph[dest - 1].append(depart - 1)

    answer = 0
    def bfs(curr, graph, visited):
        nonlocal answer
        q = deque([curr])
        visited[curr] = 1
        while q:
            v = q.popleft()
            for adj in graph[v]:
                if not visited[adj]:
                    q.append(adj)
                    answer += 1
                    visited[adj] = 1
    bfs(0, graph, visited)
    print(answer)
    return [str(answer)]

if __name__ == "__main__":
    main()