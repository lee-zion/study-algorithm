import sys
from math import isqrt, pow

def main():
    answer = []
    T = int(sys.stdin.readline().strip())
    for i in range(T):
        depart, dest = map(int, sys.stdin.readline().strip().split())
        diff = dest - depart
        n = int(isqrt(diff))
        n2 = pow(n, 2)
        if diff == n2:
            print(2*n - 1)
        elif diff <= n2 + n:
            print(2*n)
        else:
            print(2*n + 1)

if __name__ == "__main__":
    main()