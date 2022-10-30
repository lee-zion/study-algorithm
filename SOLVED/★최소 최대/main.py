import sys

def main():
    LIMIT = 10**6 + 1
    min, max = LIMIT, -LIMIT
    N = sys.stdin.readline()
    nums = list(map(int, sys.stdin.readline().split(" ")))
    for num in nums:
        if num < min:
            min = num
        if num > max:
            max = num
    print(f"{str(min)} {str(max)}")

if __name__ == "__main__":
    main()