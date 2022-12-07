import sys

def main():
    h = int(sys.stdin.readline())
    a = []
    for depth in range(h):
        a.append(list(map(int, sys.stdin.readline().rstrip().split())))
    
    dp = [0] * h
    dp[0] = a[0][0]
    
    for depth in range(1, h):
        temp = [0] * h
        for i, v in enumerate(a[depth]):
            if i == 0:
                temp[i] = dp[i] + v
            elif i == len(a[depth]) - 1:
                temp[i] = dp[i-1] + v
            else:
                temp[i] = v + max(dp[i], dp[i-1])
        dp = temp
    print(max(dp))

if __name__ == "__main__":
    main()