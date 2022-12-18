import sys
from collections import deque

input = sys.stdin.readline
def main():
    cities, buses = map(int, (input(), input()))
    VAL_INF, KEY_INF = pow(10, 6), -1
    graph = [[VAL_INF]*(cities + 1) for _ in range(cities + 1)]
    
    for bus in range(buses):
        depart, dest, cost = map(int, input().split())
        graph[depart][dest] = cost
    
    depart, dest = map(int,input().split())
    visited = [False] * (cities + 1)
    def dijkstra(begin, dest):
        nonlocal graph, visited, VAL_INF, KEY_INF
        q = deque([begin])
        dist = [VAL_INF] * (cities + 1)
        dist[begin] = 0
        while q:
            curr = q.popleft()
            visited[curr] = True
            val_min, key_min = VAL_INF, KEY_INF
            for i_adj, adj in enumerate(graph[curr]):
                if not visited[i_adj] and adj != VAL_INF:
                    dist[i_adj] = min(dist[i_adj], dist[curr] + adj)
                    if val_min > dist[i_adj]:
                        val_min = dist[i_adj]
                        key_min = i_adj
            if key_min != KEY_INF:
                next = key_min
                q.append(next)
        return dist[dest]
    print(dijkstra(depart, dest))

if __name__ == "__main__":
    main()