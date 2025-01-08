import sys
input = sys.stdin.readline

def main():
    # your code here
    n, target = map(int, input().strip().split())
    coins = []
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(n):
        coins.append(int(input().strip()))
    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] += dp[i - coin]
    print(dp[target])
if __name__ == "__main__":
    main()