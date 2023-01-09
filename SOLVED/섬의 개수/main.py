import sys
from collections import deque
input = sys.stdin.readline

def main():
    LAND = 1
    dx = [0,  0,  1, 1, 1, -1, -1, -1]
    dy = [1, -1, -1, 0, 1, -1,  0,  1]
    while True:
        Y_MAX, X_MAX = map(int, input().strip().split())
        if Y_MAX == 0 and X_MAX == 0:
            break
        visited = [[False] * Y_MAX for _ in range(X_MAX)]
        maps = []
        for x in range(X_MAX):
            maps.append(list(map(int, input().strip().split())))
        answer = 0

        def bfs(x0, y0):
            nonlocal visited, maps, dx, dy, Y_MAX, X_MAX, LAND
            q = deque([(x0, y0)])
            while q:
                x, y = q.popleft()
                if not visited[x][y]:
                    visited[x][y] = True
                    for i in range(8):
                        nx, ny = x + dx[i], y + dy[i]
                        if nx >= X_MAX or ny >= Y_MAX or nx < 0 or ny < 0:
                            continue
                        if not visited[nx][ny] and maps[nx][ny] == LAND:
                            q.append((nx, ny))
        lands = []
        for x in range(X_MAX):
            for y in range(Y_MAX):
                if maps[x][y] == LAND:
                    lands.append((x, y))
        if Y_MAX == X_MAX == 1:
            # dot shape
            answer = maps[0][0]
        else:
            for x, y in lands:
                if not visited[x][y]:
                    bfs(x, y)
                    answer += 1
        print(answer)

if __name__ == "__main__":
    main()