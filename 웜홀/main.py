from sys import stdin

def main():
    T = int(stdin.readline())
    GRAPH_INIT = 10**4 + 1
    for i in range(T):
        n, m, w = map(int, stdin.readline().split())

        roads = []
        for _ in range(1, m + 1):
            roads.append(list(map(int, stdin.readline().split())))
        holes = []
        for _ in range(1, w + 1):
            holes.append(list(map(int, stdin.readline().split())))
        graph = [[GRAPH_INIT] * (n) for _ in range(n)]
        for s, e, t in roads:
            graph[s - 1][e - 1] = min(graph[s - 1][e - 1], t)
            graph[e - 1][s - 1] = min(graph[e - 1][s - 1], t)
        for s, e, t in holes:
            graph[s - 1][e - 1] = -t

        for i in range(n):
            for j in range(n):
                if graph[i][j] == GRAPH_INIT:
                    graph[i][j] = 0

        def dfs(time, curr, graph, visited):
            nonlocal answer, begin
            if curr == begin:
                answer = min(answer, time)
            else:
                for col, adj in enumerate(graph[curr]):
                    if not visited[col] and adj != 0:
                        visited[col] = True
                        dfs(time + adj, col, graph, visited)
                        visited[col] = False

        answer = 0
        for begin in range(n):
            answer = GRAPH_INIT
            visited = [False] * (n + 1)
            for row, adj in enumerate(graph[begin]):
                dfs(adj, row, graph, visited)
                if answer < 0:
                    answer = "YES"
                    break
            if answer != "YES":
                answer = "NO"
        print(answer)


if __name__ == "__main__":
    main()
