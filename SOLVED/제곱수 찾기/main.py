import sys
from math import isqrt

def main():
    n, m = map(int, sys.stdin.readline().strip().split())
    graph = [sys.stdin.readline().strip() for i in range(n)]
    answer = -1
    pool = set()
    for x in range(n):
        for y in range(m):
            for dx in range(-n, n):
                for dy in range(-m, m):
                    nx, ny, temp = x, y, ""
                    while 0 <= nx < n and 0 <= ny < m:
                        temp += graph[nx][ny]
                        if dx == 0 and dy == 0:
                            break
                        itemp = int(temp)
                        if isqrt(itemp) ** 2 == itemp:
                            answer = max(answer, itemp)
                        nx += dx
                        ny += dy
    print(answer)

if __name__ == "__main__":
    main()