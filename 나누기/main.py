import sys

def main():
    tabs = [list(map(int, line.split())) for line in sys.stdin.readlines()]
    s = "is not an integer with less than 100 digits."
    for t, a, b in tabs:
        u = f"({t}^{a}-1)/({t}^{b}-1)"
        num = pow(t, a) - 1
        den = pow(t, b) - 1
        if num % den:
            print(f"{u} {s}")
            continue
        result = num // den
        if len(str(result)) < 100:
            print(f"{u} {result}")
        else:
            print(f"{u} {s}")
if __name__ == "__main__":
    main()