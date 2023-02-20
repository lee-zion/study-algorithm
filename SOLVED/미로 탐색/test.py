import unittest
from traceback import print_exception
import sys
from collections import deque

def read_file(filename):
    file = open(filename, 'r')
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret

def main(inputs):
    answers = []
    try:
        for input in inputs:
            """
            0: no 1: movable
            (1,1) to (n,m)
            """
            # your code here
            n, m = map(int, input[0].split())
            dist = [[1] * m for _ in range(n)]
            maze = []
            for i in range(n):
                maze.append(list(map(int, input[1+i])))
            q = deque([])
            visited = set()
            pos_init = (0, 0)
            q.append(pos_init)
            visited.add(pos_init)
            answer = 0
            while q:
                x, y = q.popleft()
                if x == n-1 and y == m-1:
                    break
                dx = [0, 1, 0, -1]
                dy = [1, 0, -1, 0]
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if nx < 0 or ny < 0 or nx >= n or ny >= m:
                        continue
                    if maze[nx][ny] == 0:
                        continue
                    if maze[nx][ny] == 1 and (nx, ny) not in visited:
                        q.append((nx, ny))
                        visited.add((nx, ny))
                        dist[nx][ny] = dist[x][y] + 1
            answers.append(dist[n-1][m-1])
        return answers
    except Exception:
        print(f"===========================================================================")
        print(f"Failed in the case below")
        print(f"input: {input}")
        exc_info = sys.exc_info()
        print_exception(*exc_info)
        print(f"===========================================================================")
        del exc_info
class TestCases(unittest.TestCase):
    def test_input_txt(self):
        inputs, answers = [], []
        for i in range(1, 4 + 1):
            inputs.append(read_file(f"미로 탐색/input{i}.txt"))
            answers.append(int(read_file(f"미로 탐색/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()