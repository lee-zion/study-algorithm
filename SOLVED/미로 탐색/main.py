import sys
input = sys.stdin.readline
from collections import deque

def main():
    n, m = map(int, input().strip().split())
    dist = [[1] * m for _ in range(n)]
    maze = []
    for i in range(n):
        maze.append(list(map(int, input().strip())))
    q = deque([])
    visited = set()
    q.append((0, 0))
    visited.add((0, 0))
    while q:
        x, y = q.popleft()
        if x == n-1 and y == m-1:
            break
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if maze[nx][ny] == 0:
                continue
            if maze[nx][ny] == 1 and (nx, ny) not in visited:
                q.append((nx, ny))
                visited.add((nx, ny))
                dist[nx][ny] = dist[x][y] + 1
    print(dist[n-1][m-1])

if __name__ == "__main__":
    main()