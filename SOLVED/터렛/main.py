import sys, math

def main():
    T = int(sys.stdin.readline())
    for it in range(T):
        answer = None
        x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().rstrip().split())
        if r2 > r1:
            x1, y1, r1, x2, y2, r2 = x2, y2, r2, x1, y1, r1
        if x1 == x2 and y1 == y2:
            answer = -1 if r1 == r2 else 0
        else:
            d = math.sqrt(pow(abs(x1 - x2), 2) + pow(abs(y1 - y2), 2))
            answer = 0 if d > r1 + r2 else 1 if d == r1 + r2 else 0 if d + r2 < r1 else 1 if r1 == r2 + d else 2
        print(answer)

if __name__ == "__main__":
    main()