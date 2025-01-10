import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def main():
    T = int(input())
    for t in range(T):
        heap_min, heap_max = [], []
        valid = {}
        idx = 0
        K = int(input().strip())
        for _ in range(K):
            oper, num = input().strip().split()
            num = int(num)
            if oper == "I":
                heappush(heap_max, (-num, idx))
                heappush(heap_min, (num, idx))
                valid[idx] = True
                idx += 1
            elif oper == "D":
                if num > 0:
                    while heap_max and not valid.get(heap_max[0][1], False):
                        heappop(heap_max)
                    if heap_max:
                        val, idx_remove = heappop(heap_max)
                        valid[idx_remove] = False
                else:
                    while heap_min and not valid.get(heap_min[0][1], False):
                        heappop(heap_min)
                    if heap_min:
                        val, idx_remove = heappop(heap_min)
                        valid[idx_remove] = False
        
        while heap_max and not valid.get(heap_max[0][1], False):
            heappop(heap_max)
        while heap_min and not valid.get(heap_min[0][1], False):
            heappop(heap_min)
        
        answer = "EMPTY"
        if heap_max and heap_min:
            answer = f"{-heap_max[0][0]} {heap_min[0][0]}"
        print(answer)

if __name__ == "__main__":
    main()