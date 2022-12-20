import sys
input = sys.stdin.readline

def main():
    n_cities, n_buses = map(int, [input(), input()])
    n_vertex, VAL_INF = n_cities + 1, pow(10, 10) + 1
    graph = [[VAL_INF] * (n_vertex) for _ in range(n_vertex)]
    for i in range(n_vertex):
        graph[i][i] = 0
    for _ in range(n_buses):
        depart, dest, cost = map(int, input().split())
        graph[depart][dest] = min(graph[depart][dest], cost)
    
    def floyd(graph):
        nonlocal n_vertex
        for k in range(1, n_vertex):
            for i in range(1, n_vertex):
                for j in range(1, n_vertex):
                    dist_curr = graph[i][k] + graph[k][j]
                    graph[i][j] = min(graph[i][j], dist_curr)
        for i in range(1, n_vertex):
            for j in range(1, n_vertex):
                if graph[i][j] == VAL_INF:
                    graph[i][j] = 0
        [print(j) for j in [" ".join(map(str, i[1:])) for i in graph[1:]]]
    
    floyd(graph)

if __name__ == "__main__":
    main()