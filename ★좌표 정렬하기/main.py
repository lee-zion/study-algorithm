import sys

def main():
    N = sys.stdin.readline()
    pos = []
    for i in range(int(N)):
        pos.append(list(map(int, sys.stdin.readline().split(" "))))
    pos.sort(key=lambda x: (x[0], x[1]))
    for x, y in pos:
        print(f"{x} {y}")

if __name__ == "__main__":
    main()