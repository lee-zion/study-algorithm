import sys, itertools
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    nums = input().split()
    comb = itertools.combinations_with_replacement(sorted(nums, 
    key=int), m)
    for i in list(dict.fromkeys(comb)):
        print(' '.join(i))

if __name__ == "__main__":
    main()