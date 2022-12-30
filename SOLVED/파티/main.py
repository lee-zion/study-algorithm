import sys
from collections import defaultdict
from heapq import heappop, heappush

def main():
    n, m, x = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)
    graph_rev = defaultdict(list)
    for _ in range(m):
        depart, dest, cost = map(int, sys.stdin.readline().strip().split())
        l = [i[0] for i in graph[depart]]
        if dest in l:
            idx = l.index(dest)
            graph[depart][idx] = (dest, min(graph[depart][idx][1], cost))
        else:
            graph[depart].append((dest, cost))
        
        l_rev = [i[0] for i in graph_rev[dest]]
        if depart in l_rev:
            idx = l_rev.index(depart)
            graph_rev[dest][idx] = (depart, min(graph_rev[dest][idx][1], cost))
        else:
            graph_rev[dest].append((depart, cost))

    def dijkstra(begin, graph):
        nonlocal visited
        VAL_INF = 1000001
        heap = []
        heappush(heap, (begin, 0))
        dist = [VAL_INF] * (n+1)
        dist[begin] = 0

        while heap:
            curr_i, curr_cost = heappop(heap)
            for adj_i, adj_cost in graph[curr_i]:
                total_cost = curr_cost + adj_cost
                if dist[adj_i] > total_cost:
                    dist[adj_i] = total_cost
                    heappush(heap, (adj_i, total_cost))
        return dist[1:]

    visited = [False] * (n + 1)
    to_party = dijkstra(x, graph_rev)
    visited = [False] * (n + 1)
    to_home = dijkstra(x, graph)
    print(max([i+j for i, j in zip(to_party, to_home)]))

if __name__ == "__main__":
    main()