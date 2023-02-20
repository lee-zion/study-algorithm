import sys
from collections import deque
input = sys.stdin.readline

def main():
    dep, arr = map(int, input().strip().split())
    INF = max(dep, arr)
    dist = [INF] * INF * 2
    answer = INF
    q = deque([dep])
    dist[dep] = 0
    while q:
        current = q.popleft()
        if current == arr:
            answer = dist[arr]
            break
        warp = current * 2
        if warp < INF * 2 and dist[warp] > dist[current]:
            dist[warp] = dist[current] 
            q.append(warp)
        left, right = current - 1, current + 1
        if left >= 0 and dist[left] > dist[current]:
            dist[left] = dist[current] + 1
            q.append(left)
        if right < INF * 2 and dist[right] > dist[current]:
            dist[right] = dist[current] + 1
            q.append(right)
    print(answer)

if __name__ == "__main__":
    main()