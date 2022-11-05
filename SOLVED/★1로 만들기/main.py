import sys

def main_dp():
    target = int(sys.stdin.readline())
    dp = [0] * target
    for i in range(1, target):
        dp[i] = dp[i - 1] + 1
        if (i+1) % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
        if (i+1) % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
    print(dp[-1])

if __name__ == "__main__":
    main_dp()