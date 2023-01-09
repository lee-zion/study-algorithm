import sys
input = sys.stdin.readline

def main():
    n = int(input().strip())
    A = list(map(int, input().strip().split()))
    sA = sorted(range(n), key=lambda x: A[x])
    answer = sorted(range(n), key=lambda x: sA[x])
    print(" ".join(map(str, answer)))

if __name__ == "__main__":
    main()