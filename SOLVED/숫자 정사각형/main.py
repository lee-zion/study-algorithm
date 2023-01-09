import sys
input = sys.stdin.readline

def main():
    xM, yM = map(int, input().strip().split())
    rect = []
    answer = 0
    for i in range(xM):
        rect.append(input().strip())
    for side in range(min(xM, yM) + 1):
        for x in range(xM - side):
            for y in range(yM - side):
                point = rect[x][y]
                dx = [0, side, side]
                dy = [side, 0, side]
                for i in range(3):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if rect[x][y] == rect[nx][ny]:
                        continue
                    else:
                        point = -1
                        break
                if point == -1:
                    continue
                answer = max(answer, (side+1)**2)
    print(answer)

if __name__ == "__main__":
    main()