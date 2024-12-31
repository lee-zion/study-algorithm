import sys
input = sys.stdin.readline

def main():
    # your code here
    n = int(input().strip())
    nums = []
    for i in range(n):
        num = int(input().strip())
        nums.append(num)
    
    target = max(nums) + 1
    dp = [0 for _ in range(max(target, 3))]
    dp[0] = dp[1] = 1
    dp[2] = 2
    
    for i in range(3, target):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
    for num in nums:
        print(dp[num])

if __name__ == "__main__":
    main()