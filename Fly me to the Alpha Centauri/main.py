import sys
from math import log2, pow

def main():
    answer = []
    T = int(sys.stdin.readline().strip())
    for i in range(T):
        depart, dest = map(int, sys.stdin.readline().strip().split())
        diff = dest - depart
        n = int(log2(diff))
        n2 = pow(n, 2)
        if diff == n2:
            print(2*n - 1)
        elif diff > n2 + n:
            print(2*n + 1)
        else:
            print(2*n)

if __name__ == "__main__":
    main()