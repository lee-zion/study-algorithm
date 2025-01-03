import sys
from collections import deque
input = sys.stdin.readline

def main():
    # your code here
    x_max, y_max = map(int, input().strip().split())
    answer = [["0"] * y_max for _ in range(x_max)]
    grid = list()
    plan = deque()
    visited = set()
    VISITABLE, ORIGIN = 1, 2
    UNREACHABLE = "-1"

    for i in range(x_max):
        l = list(map(int, input().strip().split()))
        grid.append(l)
        try:
            idx = l.index(ORIGIN)
            visited.add((i, idx))
            plan.append((i, idx, 0))
        except ValueError:
            continue
    
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
    while plan:
        x, y, dist = plan.popleft()
        answer[x][y] = str(dist)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= x_max or ny >= y_max:
                continue
            if (nx, ny) not in visited and grid[nx][ny] == VISITABLE:
                visited.add((nx, ny))
                plan.append((nx, ny, dist+1))
    for x in range(x_max):
        for y in range(y_max):
            if grid[x][y] == VISITABLE and (x, y) not in visited:
                answer[x][y] = UNREACHABLE
    for line in answer:
        print(" ".join(line))

if __name__ == "__main__":
    main()