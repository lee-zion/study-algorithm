import sys
from decimal import setcontext, Context, Decimal, ROUND_CEILING
setcontext(Context(prec=12))
input = sys.stdin.readline

def main():
    den, num = map(Decimal, input().strip().split())
    b34 = (1 - num / den * 10**2 % 1) / 100
    det = (1 - b34) * den - num
    print(int((b34 * den**2 / det).to_integral_exact(rounding=ROUND_CEILING)) if det > 0 else -1)

if __name__ == "__main__":
    main()