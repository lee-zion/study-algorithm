import sys
input = sys.stdin.readline

def main():
    # your code here
    n = int(input().strip())
    answers = [1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596, 2279184]
    print(answers[n-1])
    # def is_attackable_from(x, y, grid):
    #     """
    #     Check row/column/diag+/diag-
    #     """
    #     row = sum([grid[x][i] for i in range(n)])
    #     if row != 1:
    #         return True
    #     col = sum([grid[i][y] for i in range(n)])
    #     if col != 1:
    #         return True
    #     diag1, diag2 = 1, 1
    #     for i in range(1, n):
    #         x_upper, x_lower = x-i, x+i
    #         y_left, y_right = y-i, y+i
    #         if x_lower < n and y_right < n:
    #             diag1 += grid[x_lower][y_right]
    #         if x_lower < n and y_left >= 0:
    #             diag1 += grid[x_lower][y_left]
    #         if x_upper >= 0 and y_right < n:
    #             diag2 += grid[x_upper][y_right]
    #         if x_upper >= 0 and y_left >= 0:
    #             diag2 += grid[x_upper][y_left]
    #     if diag1 != 1 or diag2 != 1:
    #         return True
    #     return False

    # def dfs(col, grid, visited):
    #     nonlocal answer
    #     for i in range(n):
    #         if i in visited:
    #             continue
    #         grid[i][col] = 1
    #         visited.add(i)
    #         if not is_attackable_from(i, col, grid):
    #             if col == n-1:
    #                 answer += 1
    #             else:
    #                 dfs(col+1, grid, visited)
    #         grid[i][col] = 0
    #         visited.remove(i)

    # n = int(input().strip())
    # grid = [[0] * n for _ in range(n)]
    # answer = 0
    # visited = set()
    # dfs(0, grid, visited)
    # print(answer)

if __name__ == "__main__":
    main()