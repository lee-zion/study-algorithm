import sys

def main():
    a, b, n = map(int, sys.stdin.readline().split())
    s = str(a/b).split(".")[1]
    answer = 0 if len(s) < n else int(s[n-1])
    print(answer)

if __name__ == "__main__":
    main()