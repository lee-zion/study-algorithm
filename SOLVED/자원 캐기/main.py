import sys
input = sys.stdin.readline

def main():
    X_MAX, Y_MAX = map(int, input().split())
    land = [list(map(int, input().split())) for _ in range(X_MAX)]
    for x in range(X_MAX):
        for y in range(Y_MAX):
            left = land[x][y-1] if y > 0 else 0
            upper = land[x-1][y] if x > 0 else 0
            land[x][y] = land[x][y] + max(left, upper)
    print(land[X_MAX-1][Y_MAX-1])

if __name__ == "__main__":
    main()