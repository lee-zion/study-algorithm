import sys
from collections import deque

def main():
    dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
    graph = []
    [COL_MAX, ROW_MAX] = map(int, sys.stdin.readline().split(" "))
    for row in range(ROW_MAX):
        graph.append(list(map(int, sys.stdin.readline().split(" "))))
    
    q = deque([])
    for col in range(COL_MAX):
        for row in range(ROW_MAX):
            if graph[row][col] == 1:
                q.append((row, col))
    
    while q:
        (x, y) = q.popleft()
        curr = graph[x][y]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx > ROW_MAX - 1 or ny < 0 or ny > COL_MAX - 1:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = curr + 1
                q.append((nx, ny))
    
    day = -1
    for row in graph:
        for element in row:
            if element == 0:
                print(day)
                return day
        day = max(day, max(row))
    print(day-1)
    return day-1

if __name__ == "__main__":
    main()