import sys
input = sys.stdin.readline

def main():
    target = int(input())
    IDX, VAL = 0, 1
    dp = [[0] * 2 for _ in range(target+1)]
    for i in range(2, target+1):
        dp[i][IDX] = dp[i-1][IDX] + 1
        dp[i][VAL] = i - 1
        if i % 2 == 0:
            if dp[i][IDX] > dp[i // 2][IDX] + 1:
                dp[i][IDX] = dp[i // 2][IDX] + 1
                dp[i][VAL] = i // 2
        if i % 3 == 0:
            if dp[i][IDX] > dp[i // 3][IDX] + 1:
                dp[i][IDX] = dp[i // 3][IDX] + 1
                dp[i][VAL] = i // 3
    trace = [target]
    idx = -1
    while dp[idx][VAL]:
        trace.append(dp[idx][VAL])
        idx = dp[idx][VAL]
    print(dp[-1][IDX])
    print(' '.join(map(str, trace)))

if __name__ == "__main__":
    main()