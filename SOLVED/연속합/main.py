import sys
input = sys.stdin.readline

def main():
    n = int(input().strip())
    num = list(map(int, input().strip().split()))
    dp = [num[0]] * n
    for i in range(1, n):
        dp[i] = max(dp[i-1] + num[i], num[i])
    print(max(dp))

if __name__ == "__main__":
    main()