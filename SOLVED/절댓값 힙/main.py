import sys
from heapq import heappop, heappush
def main():
    n = int(sys.stdin.readline())
    answer = 0
    h = []
    for i in range(n):
        m = int(sys.stdin.readline())
        if m < 0:
            heappush(h, (-m, -1))
        elif m > 0:
            heappush(h, (m, 1))
        else:
            try:
                num, sign = heappop(h)
                answer = num*sign
            except IndexError:
                answer = 0
            finally:
                print(answer)

if __name__ == "__main__":
    main()