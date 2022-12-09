from sys import stdin
from heapq import heappop, heappush
input = stdin.readline

def main():
    n = int(input())
    nums = []
    for i in range(n):
        temp = int(input())
        if temp:
            heappush(nums, temp)
        else:
            if nums:
                print(heappop(nums))
            else:
                print(0)

if __name__ == "__main__":
    main()