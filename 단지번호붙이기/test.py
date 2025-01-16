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
            answer = True
            n = int(input[0])
            graph = []
            for i in range(1, n+1):
                graph.append(input[i])
            groups = []

            visited = set()
            dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
            EMPTY, HOME = "0", "1"
            for x in range(n):
                for y in range(n):
                    point = (x, y)
                    if graph[x][y] == EMPTY or point in visited:
                        continue
                    q = deque([point])
                    visited.add(point)
                    group = 1
                    while q:
                        xp, yp = q.popleft()
                        for i in range(4):
                            nx, ny = xp + dx[i], yp + dy[i]
                            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                                continue
                            if (nx, ny) not in visited and graph[nx][ny] == HOME:
                                q.appendleft((nx, ny))
                                visited.add((nx, ny))
                                group += 1
                    groups.append(group)
            groups.sort()
            answer = [len(groups), [i for i in groups]]

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
            inputs.append(read_file(f"단지번호붙이기/input{i}.txt"))
            answers.append(read_file(f"단지번호붙이기/output{i}.txt"))
        self.assertEqual([main(inputs)], answers)


if __name__ == '__main__':
    unittest.main()