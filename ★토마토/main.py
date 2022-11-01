import sys
from collections import deque

def main():
    dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
    already_done, day, graph = True, -1, []
    [COL_MAX, ROW_MAX] = map(int, sys.stdin.readline().split(" "))
    visited = [ [False]*COL_MAX for _ in range(ROW_MAX)]
    for row in range(ROW_MAX):
        graph.append(list(map(int, sys.stdin.readline().split(" "))))
    
    for row in range(ROW_MAX):
        if 0 in graph[row]:
            already_done = False
            break
    if already_done:
        day = 0
        print(day)
        return day
    q = deque([])
    for col in range(COL_MAX):
        for row in range(ROW_MAX):
            if graph[row][col] != -1:
                is_solvable = False
                for i in range(4):
                    nx, ny = row + dx[i], col + dy[i]
                    if nx < 0 or nx > ROW_MAX - 1 or ny < 0 or ny > COL_MAX-1:
                        continue
                    if graph[nx][ny] != -1:
                        is_solvable = True
                        break
                if not is_solvable:
                    print(day)
                    return day
            if graph[row][col] == 1:
                q.append((row, col))
                visited[row][col] = True
    tomorrow = [0]
    while tomorrow:
        tomorrow = []
        while q:
            (x, y) = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx > ROW_MAX - 1 or ny < 0 or ny > COL_MAX-1:
                    continue
                if graph[nx][ny] == 0 and not visited[nx][ny]:
                    graph[nx][ny] = 1
                    visited[nx][ny] = True
                    tomorrow.append((nx, ny))
        day += 1
        q = deque(tomorrow)
    print(day)
    return day

if __name__ == "__main__":
    main()