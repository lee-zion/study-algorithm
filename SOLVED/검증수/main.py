import sys

def main():
    print(sum([pow(x, 2) for x in list(map(int, sys.stdin.readline().rstrip().split()))]) % 10)

if __name__ == "__main__":
    main()