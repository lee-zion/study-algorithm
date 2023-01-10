import sys
input = sys.stdin.readline
from bisect import bisect_left

def main():
    def lis(seq: list):
        lis = [seq[0]]
        for i in range(1, len(seq)):
            if seq[i] < lis[-1]:
                idx = bisect_left(lis, seq[i])
                lis[idx] = seq[i]
            elif seq[i] > lis[-1]:
                lis.append(seq[i])
        return lis
    n = int(input())
    nums = list(map(int, input().strip().split()))
    answer = lis(nums)
    print(len(answer))

if __name__ == "__main__":
    main()