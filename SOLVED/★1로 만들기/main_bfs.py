import sys

def main():
    target = int(sys.stdin.readline())
    dp = [0] * target
    for i in range(target):
        if i % 3 == 0:
            dp[i] += i // 3
        if i % 2 == 0 and i % 3 != 0:
            dp[i] += i // 2
        if not dp[i]:
            dp[i] = dp[i - 1] + 1
    print(dp[target-1])

if __name__ == "__main__":
    main()