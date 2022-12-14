import sys, itertools

def main():
    n, m = map(int, sys.stdin.readline().split())
    num = [str(i) for i in range(1, n+1)]
    for i in [' '.join(i) for i in itertools.combinations(num, m)]:
        print(i)

if __name__ == "__main__":
    main()