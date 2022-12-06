import sys

def main():
    x, y, w, h = map(int, sys.stdin.readline().rstrip().split())
    print(min(x, abs(x-w), y, abs(y-h)))

if __name__ == "__main__":
    main()