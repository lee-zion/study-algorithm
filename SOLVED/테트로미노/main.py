import sys

def main():
    ROW_MAX, COL_MAX = map(int, sys.stdin.readline().rstrip().split())
    graph = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(ROW_MAX)]
    warrier = [
        [
            [0, 0, 1, 1], # dx
            [0, 1, 0, 1], # dy
        ]
    ]
    archer = [
        [
            [0, 0, 0, 0],
            [0, 1, 2, 3]
        ],
        [
            [0, 1, 2, 3],
            [0, 0, 0, 0]
        ],
    ]
    magician = [
        [
            [0, 1, 2, 1],
            [0, 0, 0, 1]
        ],
        [
            [1, 0, 1, 2],
            [0, 1, 1, 1]
        ],
        [
            [0, 0, 1, 0],
            [0, 1, 1, 2]
        ],
        [
            [1, 0, 1, 1],
            [0, 1, 1, 2]
        ],
    ]
    thief = [
        [
            [0, 1, 2, 0],
            [0, 0, 0, 1]
        ],
        [
            [0, 1, 2, 2],
            [0, 0, 0, 1]
        ],
        [
            [0, 0, 1, 2],
            [0, 1, 1, 1]
        ],
        [
            [0, 1, 2, 2],
            [1, 1, 1, 0]
        ],
        [
            [0, 0, 0, 1],
            [0, 1, 2, 2]
        ],
        [
            [0, 0, 0, 1],
            [0, 1, 2, 0]
        ],
        [
            [1, 1, 1, 0],
            [0, 1, 2, 2]
        ],
        [
            [0, 1, 1, 1],
            [0, 0, 1, 2]
        ],
    ]
    pirate = [
        [
            [0, 1, 1, 2],
            [0, 0, 1, 1]
        ],
        [
            [0, 1, 1, 2],
            [1, 0, 1, 0]
        ],
        [
            [0, 0, 1, 1],
            [0, 1, 1, 2]
        ],
        [
            [1, 0, 1, 0],
            [0, 1, 1, 2]
        ],
    ]
    answer = 0
    for x in range(ROW_MAX):
        for y in range(COL_MAX):
            for type in [warrier, archer, magician, thief, pirate]:
                for [dx, dy] in type:
                    temp = 0
                    for i in range(4):
                        nx, ny = x + dx[i], y + dy[i]
                        if nx >= ROW_MAX or ny >= COL_MAX or nx < 0 or ny < 0:
                            temp = 0
                            break
                        temp += graph[nx][ny]
                    answer = max(answer, temp)
    print(answer)

if __name__ == "__main__":
    main()