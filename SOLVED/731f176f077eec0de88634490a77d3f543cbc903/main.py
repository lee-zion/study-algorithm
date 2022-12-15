import sys, itertools

def main():
    n, m = map(int, sys.stdin.readline().split())
    nums = sys.stdin.readline().split()
    perm = itertools.permutations(sorted(nums, key=int), m)
    print('\n'.join(' '.join(i) for i in list(dict.fromkeys(perm))))

if __name__ == "__main__":
    main()