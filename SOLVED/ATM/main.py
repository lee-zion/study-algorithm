import sys
input = sys.stdin.readline

def main():
    # your code here
    n = int(input().strip())
    nums = sorted(list(map(int, input().strip().split())))
    idxs = [i for i in range(n, 0, -1)]
    answer = sum(map(lambda a,b: a*b, nums, idxs))
    print(answer)

if __name__ == "__main__":
    main()