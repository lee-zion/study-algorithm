import sys
input = sys.stdin.readline

def main():
    def binary_search(left, right, lis, dest):
        while left < right:
            mid = (left + right) >> 1
            if lis[mid] >= dest:
                right = mid
            else:
                left = mid + 1
        return right
    def lis_nlogn(seq: list):
        lis = [seq[0]]
        for i in range(1, len(seq)):
            if seq[i] < lis[-1]:
                idx = binary_search(0, len(lis), lis, seq[i])
                lis[idx] = seq[i]
            elif seq[i] > lis[-1]:
                lis.append(seq[i])
        return lis
    n = int(input())
    nums = list(map(int, input().strip().split()))
    answer = lis_nlogn(nums)
    print(len(answer))

if __name__ == "__main__":
    main()