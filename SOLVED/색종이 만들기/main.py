import sys
input = sys.stdin.readline

def main():
    # your code here
    n = int(input().strip())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().strip().split())))

    prefix_sum = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            left = prefix_sum[x][y - 1] if y > 0 else 0
            upper = prefix_sum[x - 1][y] if x > 0 else 0
            duplicated = prefix_sum[x - 1][y - 1] if x > 0 and y > 0 else 0
            prefix_sum[x][y] = grid[x][y] + left + upper - duplicated
    
    def get_partial_sum(x1, y1, x2, y2):
        left = prefix_sum[x2][y1 - 1] if y1 > 0 else 0
        upper = prefix_sum[x1 - 1][y2] if x1 > 0 else 0
        duplicated = prefix_sum[x1 - 1][y1 - 1] if x1 > 0 and y1 > 0 else 0
        current = prefix_sum[x2][y2]
        return current - left - upper + duplicated
    
    candidnates = []
    candidnates.append((0, 0, n-1, n-1, n))
    white, blue = 0, 0
    while candidnates:
        x1, y1, x2, y2, paper = candidnates.pop()
        partial_sum = get_partial_sum(x1, y1, x2, y2)

        if partial_sum == paper * paper:
            blue += 1
        elif partial_sum == 0:
            white += 1
        else:
            x_half, y_half, paper_half = (x1 + x2) // 2, (y1 + y2) // 2, paper // 2
            candidnates.append((x1, y1, x_half, y_half, paper_half))
            candidnates.append((x_half+1, y1, x2, y_half, paper_half))
            candidnates.append((x1, y_half+1, x_half, y2, paper_half))
            candidnates.append((x_half+1, y_half+1, x2, y2, paper_half))
    print(white)
    print(blue)
if __name__ == "__main__":
    main()