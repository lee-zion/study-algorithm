import sys
input = sys.stdin.readline

def main():
    n = int(input().strip())
    snow = list(map(int, input().strip().split()))
    for i in range(n):
        allowed = 2*i + 1
        if snow[i] > allowed:
            if i != n - 1:
                snow[i+1] += snow[i] - allowed
                snow[i] = allowed
            else:
                snow[i] = allowed
    print(" ".join(map(str, snow)))
if __name__ == "__main__":
    main()