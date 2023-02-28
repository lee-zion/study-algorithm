import sys
from collections import defaultdict

input = sys.stdin.readline

position = list(map(int, input().strip().split()))
height = list(map(int, input().strip().split()))
m = int(input())

def solution(position, height, m):
    answer = -1
    """
    degree of unstability(DOU) = number of connected blocks
    remove m blocks to minimize DOU
    return minimum DOU by removing m blocks
    """
    graph = defaultdict(list)
    def get_dou():
        return 0
    n = len(height) + 1
    for i in range(1, n):
        pi = position[i-1]
        hi = height[i-1]
        for j in range(i+1, n):
            pj = position[j-1]
            if pi + hi >= pj:
                graph[i].append(j)
            else:
                break
    dou = 0
    print(graph)
    for key in graph.keys():
        curr = len(graph[key])
        for child in graph[key]:
            graph[child]
        dou = max(dou, len(graph[key]))
    print(dou)
    return answer

print(solution(position, height, m))