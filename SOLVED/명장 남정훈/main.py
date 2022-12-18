import sys

def main():
    l, r, a = map(int, sys.stdin.readline().split())
    diff = abs(l - r)
    if diff == 0:
        print(l + r + a // 2 * 2)
    elif a > diff:
        a -= diff
        print((max(l, r) + a // 2) * 2)
    else:
        print((min(l, r) + a) * 2)

if __name__ == "__main__":
    main()