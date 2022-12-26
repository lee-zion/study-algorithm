import sys, math
def main():
    n, m = map(int, sys.stdin.readline().split())
    print(math.comb(n, m))

if __name__ == "__main__":
    main()