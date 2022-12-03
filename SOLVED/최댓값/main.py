import sys

def main():
    nums = []
    for i in range(9):
        nums.append(int(sys.stdin.readline().rstrip()))
    M = max(nums)
    print(M)
    print(nums.index(M) + 1)

if __name__ == "__main__":
    main()