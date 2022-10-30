import sys
from collections import deque

def main():
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    T = sys.stdin.readline()
    answer = []
    for i in range(int(T)):
        cnt = 0
        [ROW_MAX, COL_MAX, K] = map(int, sys.stdin.readline().split(" "))
        graph = [[0]*COL_MAX for _ in range(ROW_MAX)]
        visited = [[0]*COL_MAX for _ in range(ROW_MAX)]
        for i in range(K):
            [x, y] = list(map(int, sys.stdin.readline().split(" ")))
            graph[x][y]= 1

        for row in range(ROW_MAX):
            for col in range(COL_MAX):
                if graph[row][col] != visited[row][col]:
                    visited[row][col] = 1
                    cnt += 1
                    q = deque()
                    q.append((row, col))
                    while q:
                        r, c = q.popleft()
                        for i in range(4):
                            qr = r + dx[i]
                            qc = c + dy[i]
                            if qr > ROW_MAX-1 or qc > COL_MAX-1 or qr < 0 or qc < 0:
                                continue
                            if graph[qr][qc] and not visited[qr][qc]:
                                visited[qr][qc] = 1
                                q.append((qr, qc))
        answer.append(cnt)
    for i in answer:
        print(i)
if __name__ == '__main__':
    main()