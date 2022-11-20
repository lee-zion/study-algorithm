import sys
from math import comb

def main():
    for _ in range(int(sys.stdin.readline())):
        n, m = map(int, sys.stdin.readline().split())
        print(comb(m, n))

if __name__ == "__main__":
    main()