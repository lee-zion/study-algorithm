import sys

def main():
    n_stair = int(sys.stdin.readline())
    stairs = []
    for i in range(n_stair):
        stairs.append(int(sys.stdin.readline()))
    dp = [0] * (n_stair)
    for i in range(0, 3):
        if i == 0:
            dp[i] = stairs[i]
        elif i == 1 and n_stair > 1:
            dp[i] = max(dp[i-1] + stairs[i], stairs[i])
        elif n_stair > 2:
            dp[i] = max(dp[i-2] + stairs[i], stairs[i-1] + stairs[i])
    for i in range(3, n_stair):
        dp[i] = max(dp[i-3] + stairs[i] + stairs[i-1], dp[i-2] + stairs[i])
    print(dp[-1])
if __name__ == "__main__":
    main()