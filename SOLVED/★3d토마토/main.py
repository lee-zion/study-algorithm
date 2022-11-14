import sys
from collections import deque

def main():
    [COL_MAX, ROW_MAX, H_MAX] = list(map(int, sys.stdin.readline().split(" ")))
    graph = [[[0 for _ in range(COL_MAX)] for _ in range(ROW_MAX)] for __ in range(H_MAX)]
    for height in range(H_MAX):
        for row in range(ROW_MAX):
            graph[height][row] = list(map(int, sys.stdin.readline().split(" ")))
    
    init = []
    for height in range(H_MAX):
        for row in range(ROW_MAX):
            for col in range(COL_MAX):
                if graph[height][row][col] == 1:
                    init.append((height, row, col))

    def bfs(curr, graph):
        dx, dy, dz = [0]*6, [0]*6, [0]*6
        dx[0], dx[1] = 1, -1
        dy[2], dy[3] = 1, -1
        dz[4], dz[5] = 1, -1
        q = deque(curr)
        while q:
            (z, y, x) = q.popleft()
            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i]
                nz = z + dz[i]
                if nx < 0 or ny < 0 or nz < 0 or nx >= COL_MAX or ny >= ROW_MAX or nz >= H_MAX:
                    continue
                if graph[nz][ny][nx] == 0:
                    graph[nz][ny][nx] = graph[z][y][x] + 1
                    q.append((nz, ny, nx))
    
    bfs(init, graph)
    answer = 0
    for height in range(H_MAX):
        for row in range(ROW_MAX):
            if 0 in graph[height][row]:
                print(-1)
                return
            answer = max(answer, max(graph[height][row]))
    print(answer-1)

if __name__ == "__main__":
    main()