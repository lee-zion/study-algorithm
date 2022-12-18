import sys

def main():
    n = int(sys.stdin.readline())
    [print("@"*5*n) if i < n or i >= 4*n else print("@"*n + " "*3*n + "@"*n) for i in range(5*n)]

if __name__ == "__main__":
    main()