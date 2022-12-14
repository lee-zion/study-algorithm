import sys, itertools

def main():
    n, m = map(int, sys.stdin.readline().split())
    num = sys.stdin.readline().split()
    answer = itertools.permutations(sorted(num, key=int), m)
    print('\n'.join(' '.join(i) for i in answer))


if __name__ == "__main__":
    main()