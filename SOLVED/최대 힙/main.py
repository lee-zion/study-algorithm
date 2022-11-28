import sys
from heapq import heappush, heappop

def main():
    n = int(sys.stdin.readline())
    h = []
    for i in range(n):
        m = int(sys.stdin.readline())
        answer = 0
        if m:
            heappush(h, -m)
        else:
            try:
                answer = heappop(h) * -1
            except IndexError:
                answer = 0
            finally:
                print(answer)

if __name__ == "__main__":
    main()