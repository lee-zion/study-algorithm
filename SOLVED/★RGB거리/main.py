import sys

def main():
    n_house = int(sys.stdin.readline())
    dp = [[0] * 3 for _ in range(n_house)]
    cost = []
    for i in range(n_house):
        cost.append(list(map(int, sys.stdin.readline().split(" "))))

    for color in range(3):
        dp[0][color] = cost[0][color]
    for i in range(1, n_house):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + cost[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + cost[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + cost[i][2]
    answer = min(dp[-1])
    print(answer)

if __name__ == "__main__":
    main()