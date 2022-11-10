import sys

def main():
    n_stair = int(sys.stdin.readline())
    stairs = []
    for i in range(n_stair):
        stairs.append(int(sys.stdin.readline()))
    def dfs(curr, visited, point):
        nonlocal stairs, answer
        if not visited[curr]:
            visited[curr] = True
            point += stairs[curr]
            if curr == len(visited) - 1:
                answer = max(answer, point)
            elif curr < len(visited) - 1:
                if curr + 2 <= len(visited) - 1:
                    dfs(curr + 2, visited, point)
                    visited[curr+2] = False
                if not visited[curr-1]:
                    dfs(curr + 1, visited, point)
                    visited[curr+1] = False
    answer = 0
    visited = [False]*n_stair
    dfs(0, visited, 0)
    visited = [False]*n_stair
    dfs(1, visited, 0)
    print(answer)

if __name__ == "__main__":
    main()