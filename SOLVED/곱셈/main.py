import sys

def main():
    def expmod(base, exp, mod):
        if exp == 0:
            return 1
        if exp == 1:
            return base % mod
        else:
            half = expmod(base, exp // 2, mod) % mod
            if exp % 2 == 0:
                return pow(half, 2) % mod
            else:
                return pow(half, 2) % mod * base % mod
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    print(expmod(a, b, c))

if __name__ == "__main__":
    main()