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
            x_max, y_max = map(int, input[0].split())
            grid = []
            begin = deque()
            for i in range(x_max):
                l = input[1+i]
                if "I" in l:
                    begin.append((i, l.index("I")))
                grid.append(input[1+i])
            answer = 0
            visited = set()
            visited.add(begin[0])
            dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
            while begin:
                x, y = begin.popleft()
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    point = (nx, ny)
                    if point in visited:
                        continue
                    if nx < 0 or ny < 0 or nx >= x_max or ny >= y_max:
                        continue
                    if grid[nx][ny] == "X":
                        continue
                    if grid[nx][ny] == "P":
                        answer += 1
                    visited.add(point)
                    begin.append(point)
            if answer == 0:
                answer = "TT"
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
        for i in range(1, 2 + 1):
            inputs.append(read_file(f"헌내기는 친구가 필요해/input{i}.txt"))
            answers.append(read_file(f"헌내기는 친구가 필요해/output{i}.txt"))
        self.assertEqual([main(inputs)], answers)


if __name__ == '__main__':
    unittest.main()