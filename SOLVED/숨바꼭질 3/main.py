import sys
from collections import deque
input = sys.stdin.readline

def main():
    # your code here
    n, k = map(int, input().strip().split())
    MAX = 100_000
    INIT = MAX + 1
    dp = [INIT] * INIT
    q = deque()
    q.append((n, 0))
    answer = INIT
    while q:
        curr, time = q.popleft()
        if curr >= k:
            answer = min(answer, time + curr - k)
            continue
        
        dp[curr] = time
        i = 2
        while curr > 0:
            if dp[curr * i] > dp[curr]:
                dp[curr * i] = min(dp[curr * i], dp[curr])
                q.append((curr*i, time))
            i *= 2
            if curr * i > MAX:
                break
        if curr >= 1 and dp[curr - 1] > dp[curr]:
            dp[curr - 1] = time + 1
            q.append((curr - 1, time + 1))
        if curr <= MAX and dp[curr + 1] > dp[curr]:
            dp[curr + 1] = time + 1
            q.append((curr + 1, time + 1))
    
    print(answer)

if __name__ == "__main__":
    main()