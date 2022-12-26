import sys

def main():
    r1, s = map(int, sys.stdin.readline().split())
    print(s*2 - r1)

if __name__ == "__main__":
    main()