import unittest
from collections import deque

def read_file(filename):
    file = open(filename, 'r')
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret

def main(input):
    [COL_MAX, ROW_MAX, H_MAX] = list(map(int, input[0].split(" ")))
    graph = [[[0 for _ in range(COL_MAX)] for _ in range(ROW_MAX)] for __ in range(H_MAX)]
    # graph[height]      : height 번째 층
    # graph[height][row] : height 층의 row 행
    cnt = 0
    for height in range(H_MAX):
        for row in range(ROW_MAX):
            graph[height][row] = list(map(int, input[1+cnt].split(" ")))
            cnt += 1

    
    init = []
    for height in range(H_MAX):
        for row in range(ROW_MAX):
            for col in range(COL_MAX):
                if graph[height][row][col] == 1:
                    init.append((height, row, col))

    def bfs(curr, graph):
        dx, dy, dz = [0]*6, [0]*6, [0]*6
        dx[0], dx[1] = 1, -1 # 
        dy[2], dy[3] = 1, -1 # 
        dz[4], dz[5] = 1, -1 # 
        q = deque(curr)
        while q:
            (z, y, x) = q.popleft()
            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i]
                nz = z + dz[i]
                if nx < 0 or ny < 0 or nz < 0 or nx >= COL_MAX or ny >= ROW_MAX or nz >= H_MAX:
                    continue
                if graph[nz][ny][nx] == 0:
                    graph[nz][ny][nx] = graph[z][y][x] + 1
                    q.append((nz, ny, nx))
    
    bfs(init, graph)
    # (max element in graph - 1) is the day required
    # heapq vs max()

    # if 0 still exist, it cannot be solved
    # -> return -1
        # the condition below is the subset of the condition above
        # the condition below is included to the condition above
        # if no -1 and 1 provided, all 0 remain
        # -> return -1
    answer = 0
    for height in range(H_MAX):
        for row in range(ROW_MAX):
            if 0 in graph[height][row]:
                return ["-1"]
            answer = max(answer, max(graph[height][row]))
    return [str(answer-1)]

class TestCases(unittest.TestCase):
    def test_input_txt(self):
        input = read_file('★3d토마토/input.txt')
        answer = read_file('★3d토마토/output.txt')
        self.assertEqual(main(input), answer)


if __name__ == '__main__':
    unittest.main()