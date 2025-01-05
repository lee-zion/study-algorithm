import sys
input = sys.stdin.readline

def main():
    # your code here
    n_grid, n_problem = map(int, input().strip().split())
    grid = []
    prefix_sum = [[0] * n_grid for _ in range(n_grid)]
    for i in range(n_grid):
        grid.append(list(map(int, input().strip().split())))
    for x in range(n_grid):
        for y in range(n_grid):
            left = 0 if y == 0 else prefix_sum[x][y-1]
            top = 0 if x == 0 else prefix_sum[x-1][y]
            diag = 0 if x == 0 or y == 0 else prefix_sum[x-1][y-1]
            prefix_sum[x][y] = grid[x][y] + left + top - diag
    for i in range(n_problem):
        x1, y1, x2, y2 = map(int, input().strip().split())
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
        top = 0 if x1 == 0 else prefix_sum[x1 - 1][y2]
        left = 0 if y1 == 0 else prefix_sum[x2][y1 - 1]
        diag = 0 if x1 == 0 or y1 == 0 else prefix_sum[x1 - 1][y1 - 1]
        print(prefix_sum[x2][y2] - top - left + diag)

if __name__ == "__main__":
    main()