import sys
input = sys.stdin.readline
from collections import deque

def main():
    # your code here
    n = int(input().strip())
    lines = []
    for _ in range(n):
        lines.append(list(map(int, input().strip().split())))
    MAX = 101
    grid = [[0] * MAX for _ in range(MAX)]
    for line in lines:
        x1, y1, x2, y2 = line
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                grid[x][y] += 1
    crossed = deque()
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for x in range(MAX):
        for y in range(MAX):
            if grid[x][y] > 1:
                is_valid = True
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if nx < 0 or ny < 0 or nx >= MAX or ny >= MAX:
                        is_valid = False
                        break
                    if grid[nx][ny] == 0:
                        is_valid = False
                        break
                if is_valid:
                    crossed.append((x, y))

    answer = 0 if crossed else -1
    for cross in crossed:
        d = 1
        x, y = cross
        while True:
            is_valid = True
            dx = [d, 0, -d, 0]
            dy = [0, d, 0, -d]
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                is_pureline = True
                if dx[i]:
                    ddx = [0, 0]
                    ddy = [1, -1]
                else:
                    ddx = [1, -1]
                    ddy = [0, 0]

                for i in range(2):
                    nnx, nny = nx + ddx[i], ny + ddy[i]
                    if nny < 0 or nny >= MAX:
                        continue
                    if grid[nnx][nny] > 1:
                        is_pureline = False
                        break
                if not is_pureline:
                    is_valid = False
                    break
                if nx < 0 or ny < 0 or nx >= MAX or ny >= MAX:
                    is_valid = False
                    break
                if grid[nx][ny] == 0:
                    is_valid = False
                    break
            if not is_valid:
                break
            d += 1
        answer = max(answer, d-1)

if __name__ == "__main__":
    main()