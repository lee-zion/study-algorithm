import sys
input = sys.stdin.readline
from collections import deque

def main():
    # your code here
    x_max, y_max = map(int, input().strip().split())
    grid = []
    begin = deque()
    for i in range(x_max):
        l = input().strip()
        if "I" in l:
            begin.append((i, l.index("I")))
        grid.append(l)
    answer = 0
    visited = set()
    visited.add(begin[0])
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    while begin:
        x, y = begin.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            point = (nx, ny)
            if point in visited:
                continue
            if nx < 0 or ny < 0 or nx >= x_max or ny >= y_max:
                continue
            if grid[nx][ny] == "X":
                continue
            if grid[nx][ny] == "P":
                answer += 1
            visited.add(point)
            begin.append(point)
    if answer == 0:
        answer = "TT"
    print(answer)

if __name__ == "__main__":
    main()