from sys import stdin
input = stdin.readline

def main():
    answer = 0
    n, k = map(int, input().split())
    items = []
    for i in range(n):
        items.append(list(map(int, input().split())))
    def dfs(curr, weight, value):
        nonlocal visited, items, k, answer
        if weight <= k:
            answer = max(answer, value)
            for adj in range(n):
                if not visited[adj]:
                    visited[adj] = True
                    w, v = items[adj]
                    dfs(curr, weight + w, value + v)
                    visited[adj] = False
    for begin in range(n):
        visited = [False] * n
        visited[begin] = True
        w, v = items[begin]
        dfs(begin, w, v)
    print(answer)
    
if __name__ == "__main__":
    main()