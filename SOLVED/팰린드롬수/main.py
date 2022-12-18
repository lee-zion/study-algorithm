import sys

def main():
    ns = []
    while True:
        num = sys.stdin.readline().strip()
        if num == "0":
            break
        ns.append(num)

    for num in ns:
        n = len(num)
        n2 = n // 2
        o = 0 if n%2 == 0 else 1
        l, r = num[:n2], num[n2+o:][::-1]
        if l == r:
            print("yes")
        else:
            print("no")

if __name__ == "__main__":
    main()