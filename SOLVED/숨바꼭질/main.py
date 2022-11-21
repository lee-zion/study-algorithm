import sys
from collections import deque

def main():
    answer = None
    depart, dest = map(int, sys.stdin.readline().split())
    MAX = 2 * max(depart, dest)
    dp = [0] * (MAX + 1)
    visited = set()
    def bfs(curr, visited):
        nonlocal dest
        q = deque([curr])
        dp[curr] = 0
        visited.add(curr)
        while q:
            v = q.popleft()
            for i in range(3):
                if i == 0:
                    v_new = v * 2
                elif i == 1:
                    v_new = v + 1
                elif i == 2:
                    v_new = v - 1
                if v_new > MAX or v_new < 0 or v_new == v or v_new in visited:
                    continue
                dp[v_new] = dp[v] + 1 if dp[v_new] == 0 else min(dp[v_new], dp[v] + 1)
                q.append(v_new)
                visited.add(v_new)
                
    if depart >= dest:
        answer = str(depart - dest)
    else:
        bfs(depart, visited)
        answer = str(dp[dest])
    print(answer)

if __name__ == "__main__":
    main()