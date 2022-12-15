import sys, itertools

def main():
    n, m = map(int, sys.stdin.readline().split())
    nums = [str(i) for i in range(1, n+1)]
    comb = itertools.combinations_with_replacement(sorted(nums, key=int), m)
    print('\n'.join(' '.join(i) for i in list(dict.fromkeys(comb) )))
if __name__ == "__main__":
    main()