import sys
from collections import defaultdict, deque

def main():
    n = int(sys.stdin.readline())
    graph = defaultdict(list)
    for i in range(n-1):
        parent, child, weight = list(map(int, sys.stdin.readline().strip().split()))
        graph[parent].append((child, weight))
        graph[child].append((parent, weight))

    def get_most_far_from(begin):
        nonlocal graph, dist, i_dist, visited
        q = deque([(begin, 0)])
        while q:
            curr, acc = q.popleft()
            visited[curr] = True
            if acc > dist:
                dist = acc
                i_dist = curr
            for next, w_next in graph[curr]:
                if not visited[next]:
                    q.append((next, acc + w_next))
    
    curr = 1
    dist, i_dist = 0, -1
    visited = [False] * (n+1)
    get_most_far_from(curr)
    dist = 0
    visited = [False] * (n+1)
    get_most_far_from(i_dist)
    print(dist)

if __name__ == "__main__":
    main()