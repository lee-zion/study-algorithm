import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def main():
    def bfs(depart, dest):
        nonlocal graph, n
        visited = [False] * (n+1)
        dist_init = 0
        q = deque([(depart, dist_init)])
        while q:
            curr, dist_acc = q.popleft()
            visited[curr] = True
            if curr == dest:
                return dist_acc
            for curr_adj, curr_dist in graph[curr]:
                if not visited[curr_adj]:
                    q.append((curr_adj, dist_acc + curr_dist))
    n, m = map(int, input().strip().split())
    graph = defaultdict(list)
    for _ in range(n-1):
        x, y, dist = map(int, input().strip().split())
        graph[x].append((y, dist))
        graph[y].append((x, dist))
    for _ in range(m):
        depart, dest = map(int, input().strip().split())
        print(bfs(depart, dest))

if __name__ == "__main__":
    main()