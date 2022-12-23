import sys
input = sys.stdin.readline
def main():
    n = int(input())
    consults = []
    for curr in range(n):
        time, profit = map(int, input().split())
        consults.append((time, profit))
    dp = [0] * (n + 1)
    time, profit = consults[n-1]
    for curr in range(n-1, -1, -1):
        time, profit = consults[curr]
        if curr + time > n:
            dp[curr] = dp[curr+1]
        else:
            dp[curr] = max(dp[curr + 1], profit + dp[curr + time])
    print(dp[0])
if __name__ == "__main__":
    main()