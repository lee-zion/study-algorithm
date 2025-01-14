import sys
from collections import deque
from itertools import combinations

def main():
    x_max, y_max = map(int, input().strip().split())
    answer, graph = 0, []
    EMPTY, WALL, VIRUS = 0, 1, 2
    for _ in range(x_max):
        graph.append(list(map(int, input().strip().split())))
    
    def find(graph, val):
        nonlocal x_max, y_max
        return [(x, y) for x in range(x_max) for y in range(y_max) if graph[x][y] == val]

    def spread_virus(graph, viruses):
        nonlocal x_max, y_max, EMPTY
        dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
        q = deque(viruses)
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or ny < 0 or nx >= x_max or ny >= y_max:
                    continue
                if graph[nx][ny] == EMPTY:
                    graph[nx][ny] = VIRUS
                    q.appendleft((nx, ny))
    
    empties = find(graph, EMPTY)
    viruses = find(graph, VIRUS)
    answer = 0
    for walls in combinations(empties, 3):
        for x, y in walls:
            graph[x][y] = WALL
        
        graph_temp = [row[:] for row in graph]
        spread_virus(graph_temp, viruses)
        answer = max(answer, len(find(graph_temp, EMPTY)))
        
        for x, y in walls:
            graph[x][y] = EMPTY
    
    print(answer)

if __name__ == "__main__":
    main()