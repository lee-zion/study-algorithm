import sys
def main():
    [n, r, c] = map(int, sys.stdin.readline().split(" "))
    offset = 0
    if not (r > 2**n or c > 2**n):
        while (n > 1):
            det, adder = 2**(n-1), 4**(n-1)
            if r < det:
                if c < det:
                    None
                else:
                    offset += adder
                    c -= det
            else:
                if c < det:
                    offset += adder*2
                    r -= det
                else:
                    offset += adder*3
                    r -= det
                    c -= det
            n -= 1
            if n == 1:
                offset += 2*r + c
        print(offset)
if __name__ == "__main__":
    main()