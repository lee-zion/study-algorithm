import sys

def main():
    n = int(sys.stdin.readline())
    for star in range(1, n+1):
        print(" " * (n - star) + "*" * star)

if __name__ == "__main__":
    main()