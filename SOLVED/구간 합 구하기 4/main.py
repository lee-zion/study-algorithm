import sys
input = sys.stdin.readline

def main():
    # your code here
    n, m  = map(int, input().strip().split())
    nums = list(map(int, input().strip().split()))
    prefix_sum = [0 for _ in range(n+1)]
    for i, num in enumerate(nums):
        prefix_sum[i+1] = prefix_sum[i] + num
    
    for i in range(m):
        begin, end = map(int, input().strip().split())
        answer = prefix_sum[end] - prefix_sum[begin-1]
        print(answer)

if __name__ == "__main__":
    main()