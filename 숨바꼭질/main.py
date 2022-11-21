import sys
from collections import deque

def main():
    depart, dest = map(int, sys.stdin.readline().split())
    answer = 0
    MAX = 2*10**5
    dp = [10**5] * (MAX + 1)
    visited = [False] * (MAX + 1)
    def bfs(depart):
        nonlocal dp, dest
        destT2 = dest * 2
        dp[depart] = 0
        q = deque([depart])
        while q:
            curr = q.popleft()
            currT2 = curr * 2
            currA1 = curr + 1
            currM1 = curr - 1
            if currT2 <= MAX and currT2 <= destT2 and currT2 != curr and not visited[currT2]:
                dp[currT2] = min(dp[currT2], dp[curr] + 1)
                visited[currT2] = True
                q.append(currT2)
            if currA1 <= MAX and currA1 <= destT2 and not visited[currA1]:
                dp[currA1] = min(dp[currA1], dp[curr] + 1)
                q.append(currA1)
            if currM1 >= 0 and not visited[currM1]:
                dp[currM1] = min(dp[currM1], dp[curr] + 1)

    if depart >= dest:
        answer = depart - dest
    else:
        # depart < dest
        bfs(depart)
        answer = dp[dest]
    print(answer)

if __name__ == "__main__":
    main()