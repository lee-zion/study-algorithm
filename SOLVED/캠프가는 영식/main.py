import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def main():
    n, begin = map(int, input().strip().split())
    heap = []
    for i in range(n):
        start, interval, n_bus = map(int, input().strip().split())
        for ib in range(n_bus):
            begin_bus = start + interval*ib
            if begin <= begin_bus:
                heappush(heap, begin_bus)
    answer = heappop(heap) - begin if heap else -1
    print(answer)

if __name__ == "__main__":
    main()