import sys

def main():
    i = 0
    tests = []
    while True:
        l = list(map(int, sys.stdin.readline().split()))
        if sum(l) == 0:
            break
        tests.append(sorted(l))
        i += 1
    for a, b, c in tests:
        c2hat = a**2 + b**2
        c2 = c**2
        if c2hat == c2:
            print("right")
        else:
            print("wrong")

if __name__ == "__main__":
    main()