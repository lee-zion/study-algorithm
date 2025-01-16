import sys
from collections import deque
input = sys.stdin.readline

def main():
    # your code here
    n = int(input().strip())
    graph = []
    EMPTY, HOME = "0", "1"
    for i in range(n):
        graph.append(input().strip())
    visited = set()
    groups = []
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    for x in range(n):
        for y in range(n):
            point = (x, y)
            if graph[x][y] == EMPTY or point in visited:
                continue
            q = deque()
            q.appendleft(point)
            visited.add(point)
            group = 1
            while q:
                px, py = q.popleft()
                for i in range(4):
                    nx, ny = px + dx[i], py + dy[i]
                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        continue
                    if (nx, ny) not in visited and graph[nx][ny] == HOME:
                        q.appendleft((nx, ny))
                        visited.add((nx, ny))
                        group += 1
            groups.append(group)
    groups.sort()
    print(len(groups))
    [print(i) for i in groups]
            

if __name__ == "__main__":
    main()