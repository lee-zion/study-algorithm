import sys
from bisect import bisect_left
from collections import deque
input = sys.stdin.readline

def main():
    n = int(input())
    nums = list(map(int, input().strip().split()))

    def lis_nlogn(seq: list):
        ls = len(seq)
        lis_len = [seq[0]]
        lis_idx = [1]
        for i in range(1, ls):
            if seq[i] < lis_len[-1]:
                idx = bisect_left(lis_len, seq[i])
                lis_len[idx] = seq[i]
                lis_idx.append(idx + 1)
            elif seq[i] > lis_len[-1]:
                lis_len.append(seq[i])
                lis_idx.append(len(lis_len))
            else:
                lis_idx.append(len(lis_len))
        target = len(lis_len)
        lis = deque([])
        for i in range(ls - 1, -1, -1):
            if lis_idx[i] == target:
                target -= 1
                lis.appendleft(seq[i])
        return list(lis)
    lis = lis_nlogn(nums)
    print(f"{str(len(lis))}\n{' '.join(map(str, lis))}")
if __name__ == "__main__":
    main()