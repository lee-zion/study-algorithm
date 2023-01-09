import sys
input = sys.stdin.readline

def main():
    n = int(input())
    if n > 0 or (n < 0 and n%2 == 1):
        sign = 1
    elif n == 0:
        sign = 0
    else:
        sign = -1
    
    na = abs(n)
    dp = [0] * (na + 1)
    if na >= 1:
        dp[1] = 1
    if na >= 2:
        dp[2] = 1
    for ni in range(3, max(3, na+1)):
        dp[ni] = (dp[ni - 1] + dp[ni - 2]) % 10**9
    answer = dp[na] if n != 0 else 0
    
    print(sign)
    print(answer)

if __name__ == "__main__":
    main()