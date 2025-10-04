import sys
input = sys.stdin.readline

def main():
    # your code here
    x, y = input().strip(), input().strip()
    xm, ym = len(x), len(y)
    dp = [[0] * (ym+1) for _ in range(xm + 1)]
    for i in range(xm):
        for j in range(ym):
            if x[i] == y[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    print(dp[xm][ym])

if __name__ == "__main__":
    main()