import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    INF = 101
    n = int(input())
    p1, p2 = map(int, input().strip().split())
    m = int(input())
    parents, children = defaultdict(list), defaultdict(list)
    for i in range(m):
        a, b = map(int, input().split())
        children[a].append(b)
        parents[b].append(a)
    answer = INF
    is_finished = False
    visited = [False] * (n + 1)
    def dfs(depth, curr, end):
        nonlocal answer, parents, children, is_finished, visited
        if is_finished:
            return
        if curr == end:
            answer = min(answer, depth)
            is_finished = True
            return
        if not visited[curr]:
            visited[curr] = True
            for parent in parents[curr]:
                if not visited[parent]:
                    dfs(depth + 1, parent, end)
            for child in children[curr]:
                if not visited[child]:
                    dfs(depth + 1, child, end)
    
    dfs(0, p1, p2)
    if answer == INF:
        answer = -1
    print(answer)

if __name__ == "__main__":
    main()