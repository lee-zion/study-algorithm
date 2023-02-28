import sys
input = sys.stdin.readline

n = int(input())
chopsticks = list(map(int, input().strip().split()))

def solution(n, chopsticks):
    answer = 0
    done = [[2, 0, 0, 0], [0, 2, 0, 0], [0, 0, 2, 0], [0, 0, 0, 2]]
    board = [[0]*4 for _ in range(n)]
    for i, chop in enumerate(chopsticks):
        for c in chop:
            if c == "A":
                board[i][0] += 1
            elif c == "B":
                board[i][1] += 1
            elif c == "C":
                board[i][2] += 1
            elif c == "D":
                board[i][3] += 1

    while True:
        for b in board:
            does_one_exist = False
            for i in range(4):
                if b[i] == 1:
                    does_one_exist = True
                    break
            if does_one_exist:
                break
        if not does_one_exist:
            break
        # exchange stage
        # 같은 라인 찾기: 거리 + 사이의 2 갯수
        for i in range(n):
            curr = board[i]
            if curr in done:
                continue
            for j in range(n):
                if i == j:
                    continue
                new = board[j]
                # if there are no common: like 1100 and 0011, pass
                common_found = -1
                for k in range(4):
                    if curr[k] == 1 and new[k] == 1:
                        common_found = k
                        break
                if common_found == -1:
                    continue
                for k in range(4):
                    if k == common_found:
                        curr[k] += 1
                        new[k] -= 1
                        continue
                    if curr[k] == 1:
                        curr[k] -= 1
                        new[k] += 1
                        break
                diff = abs(i - j)
                answer += diff * 2 - 1 if diff != 1 else 1
        # update stage
        break
    return answer

print(solution(n, chopsticks))