from heapq import heapify, heappush, heappop

def solution(scoville, K):
    answer = 0
    heap = []
    for sl in scoville:
        heappush(heap, sl)

    # do mixing
    while heap:
        lowest = heappop(heap)
        if lowest > K:
            break
        if not heap:
            if lowest < K:
                answer = -1
            break
        heappush(heap, lowest + (heappop(heap) << 1))
        answer += 1
    return answer