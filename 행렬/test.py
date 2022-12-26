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
            current, target, answer = [], [], -1
            
            if x_max < 3 or y_max < 3:
                answers.append(answer)
                break
            
            for x in range(x_max):
                current.append(list(map(int, input[1 + x])))
            for x in range(x_max):
                target.append(list(map(int, input[1 + x_max + x])))
            
            
            
            def flip_from(x, y, matrix):
                nonlocal x_max, y_max
                dx = [0, 1, 2, 0, 1, 2, 0, 1, 2]
                dy = [0, 0, 0, 1, 1, 1, 2, 2, 2]
                for i in range(9):
                    nx, ny = x + dx[i], y + dy[i]
                    if nx < 0 or ny < 0 or nx >= x_max or ny >= y_max:
                        continue
                    matrix[nx][ny] = 0 if matrix[nx][ny] else 1
            
            def bfs(curr, matrix, cnt):
                nonlocal visited, ix, iy
                q = deque([curr])
                while q:
                    x, y = q.popleft()
                    visited[x][y] = True
                    dx, dy = [0, 1], [1, 0]
                    for i in range(2):
                        nx, ny = x + dx[i], y + dy[i]
                        if nx < 0 or ny < 0 or nx >= ix or ny >= iy:
                            continue
                        if not visited[nx][ny]:
                            q.append((nx, ny))
                            cnt += 1
                return cnt
            ix, iy = x_max-2, y_max-2
            visited = [[False] * iy for _ in range(ix)]
            for x in range(0, ix):
                for y in range(0, iy):
                    flip_from(x, y, current)

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
        for i in range(1, 4 + 1):
            inputs.append(read_file(f"행렬/input{i}.txt"))
            answers.append(int(read_file(f"행렬/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()