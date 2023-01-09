from heapq import heappop, heapify
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = [-i for i in map(int, input().strip().split())]
    heapify(a)
    heapify(b)
    
    answer = 0
    for i in range(n):
        answer -= heappop(a) * heappop(b)
    print(answer)

if __name__ == "__main__":
    main()