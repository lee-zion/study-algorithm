import sys

def main():
    POSSIBLE_MAX = 64
    row, col = map(int, sys.stdin.readline().split())
    board = []
    for i in range(row):
        temp = []
        for j in sys.stdin.readline().strip():
            temp.append(False) if j == "B" else temp.append(True)
        board.append(temp)
    repair_tbl = [[POSSIBLE_MAX] * (col - 7) for _ in range(row - 7) ]
    
    for x in range(row - 7):
        for y in range(col - 7):
            repair_by_case = [0, 0]
            for case in range(2):
                for dx in range(8):
                    for dy in range(8):
                        nx, ny = x + dx, y + dy
                        if (nx + ny)%2 == case:
                            if not board[nx][ny]:
                                repair_by_case[case] += 1
                        else:
                            if board[nx][ny]:
                                repair_by_case[case] += 1
            repair_tbl[x][y] = min(repair_tbl[x][y], min(repair_by_case))
    print(min([min(r) for r in repair_tbl]))

if __name__ == "__main__":
    main()