import sys
from heapq import heappop, heappush

input = sys.stdin.readline
def main():
    cities, buses = map(int, (input(), input()))
    VAL_INF, KEY_INF = pow(10, 10), -1
    graph = [[VAL_INF]*(cities + 1) for _ in range(cities + 1)]
    
    for bus in range(buses):
        depart, dest, cost = map(int, input().split())
        graph[depart][dest] = min(graph[depart][dest], cost)
    
    depart, dest = map(int,input().split())
    visited = [False] * (cities + 1)
    def dijkstra(begin, dest):
        nonlocal graph, visited, VAL_INF, KEY_INF
        heap = []
        heappush(heap, (begin, 0))
        dist = [VAL_INF] * (cities + 1)
        dist[begin] = 0
        while heap:
            idx_curr, cost_curr = heappop(heap)
            for idx_adj, cost_adj in enumerate(graph[idx_curr]):
                cost_total = cost_curr + cost_adj
                if dist[idx_adj] > cost_total:
                    dist[idx_adj] = cost_total
                    heappush(heap, (idx_adj, cost_total))
        return dist[dest]
    print(dijkstra(depart, dest))

if __name__ == "__main__":
    main()