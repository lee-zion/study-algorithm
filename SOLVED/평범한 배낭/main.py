import sys
input = sys.stdin.readline

def main():
    # your code here
    i_max, w_max = map(int, input().strip().split())
    items = []
    dp = [0] * (w_max + 1)
    for i in range(i_max):
        items.append(list(map(int, input().strip().split())))
    for item in items:
        w, v = item
        for i in range(w_max, w-1, -1):
            dp[i] = max(dp[i - w] + v, dp[i])
    print(dp[-1])

if __name__ == "__main__":
    main()