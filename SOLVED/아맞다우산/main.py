import sys
from collections import deque
from itertools import permutations
input = sys.stdin.readline

def get_next_target(target, i, exit):
        l = len(target)
        if i < l:
            return target[i]
        return exit

def main():
    # your code here
    col, row = map(int, input().strip().split())
    symbol = {
        ".": 0,
        "#": -1,
        "S": 1,
        "X": 2,
        "E": 3
    }
    house = []
    begin, target_list, exit = None, [], None
    for x in range(row):
        temp = []
        for y, s in enumerate(input().strip()):
            s_parsed = symbol[s]
            temp.append(s_parsed)
            if s_parsed == 2:
                target_list.append((x, y))
                continue
            elif s_parsed == 1:
                begin = (x, y, 0)
                continue
            elif s_parsed == 3:
                exit = (x, y)
                continue
        house.append(temp)
    
    
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
    INF = 2500
    answer = INF

    comb = permutations(target_list, len(target_list))
    for target in comb:
        q = deque([begin])
        x, y, _ = begin
        visited = [[False] * col for _ in range(row)]
        visited[x][y] = True
        ti = 0
        target = list(target)
        dest = get_next_target(target, ti, exit)
        while q:
            x, y, time = q.popleft()
            if (x, y) == dest:
                if dest == exit:
                    break
                ti += 1
                dest = get_next_target(target, ti, exit)
                visited = [[False] * col for _ in range(row)]
                visited[x][y] = True
                q.clear()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= row or ny < 0 or ny >= col:
                    continue
                if visited[nx][ny]:
                    continue
                if house[nx][ny] < 0:
                    continue
                q.append((nx, ny, time + 1))
                visited[nx][ny] = True
        answer = min(answer, time)
    print(answer)
if __name__ == "__main__":
    main()