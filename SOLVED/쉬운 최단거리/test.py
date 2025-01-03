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
            # your code here
            """
            목표지점(2)에서 모든 갈 수 있는 땅(1)까지의 최소거리 기록
            visited 확인
            """
            x_max, y_max = map(int, input[0].split())
            answer = [[0] * y_max for _ in range(x_max)]
            VISITABLE, ORIGIN = 1, 2
            grid = list()
            plan = deque()
            visited = set()

            for i in range(x_max):
                l = list(map(int, input[1+i].split()))
                grid.append(l)
                try:
                    idx = l.index(ORIGIN)
                    plan.append((i, idx, 0))
                    visited.add((i, idx))
                    # answer[i][idx] = 0
                except ValueError:
                    continue
            
            while plan:
                x, y, dist = plan.popleft()
                answer[x][y] = dist
                # visited.add((x, y))

                dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if nx < 0 or nx >= x_max or ny < 0 or ny >= y_max:
                        continue
                    if (nx, ny) not in visited and grid[nx][ny] == VISITABLE:
                        plan.append((nx, ny, dist+1))
                        visited.add((nx, ny))
            answers.append(answer)
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
        for i in range(1, 1 + 1):
            inputs.append(read_file(f"쉬운 최단거리/input{i}.txt"))
            answers.append(read_file(f"쉬운 최단거리/output{i}.txt"))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()