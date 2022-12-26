import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def main():
    orders = list(map(int, input().split()))[:-1]
    DP_INIT = -1
    dp = [[[DP_INIT] * 10**5 for _ in range(5)] for _ in range(5)]

    def move(prev, curr):
        if prev == 0:
            return 2
        diff = (prev - curr) % 4
        if diff == 0:
            return 1
        if diff == 2:
            return 4
        return 3
    
    def solve(l, r, n):
        nonlocal orders, dp, DP_INIT
        if n == len(orders):
            return 0

        if dp[l][r][n] != DP_INIT:
            return dp[l][r][n]
        
        dp[l][r][n] = min(move(l, orders[n]) + solve(orders[n], r, n + 1), move(r, orders[n]) + solve(l, orders[n], n + 1))

        return dp[l][r][n]
    
    print(solve(0, 0, 0))

if __name__ == "__main__":
    main()