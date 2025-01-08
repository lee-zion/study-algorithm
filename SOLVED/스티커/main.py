import sys
input = sys.stdin.readline

def main():
    # your code here
    n_test = int(input().strip())
    for _ in range(n_test):
        n = int(input().strip())
        sticker = []
        FIRST, SECOND, LEAVE = 0, 1, 2
        dp = [[0] * n for _ in range(3)]
        for i in range(2):
            sticker.append(list(map(int, input().strip().split())))
            dp[i][0] = sticker[i][0]
        for i in range(1, n):
            CURR, PREV = i, i-1
            dp[FIRST][CURR] = max(dp[SECOND][PREV] + sticker[FIRST][CURR], dp[LEAVE][PREV] + sticker[FIRST][CURR])
            dp[SECOND][CURR] = max(dp[FIRST][PREV] + sticker[SECOND][CURR], dp[LEAVE][PREV] + sticker[SECOND][CURR])
            dp[LEAVE][CURR] = max(dp[FIRST][PREV], dp[SECOND][PREV])
        print(max(dp[i][n-1] for i in range(3)))


if __name__ == "__main__":
    main()