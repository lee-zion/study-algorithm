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
            offset = 0
            SEA, LAND = 0, 1
            dx = [0,  0,  1, 1, 1, -1, -1, -1]
            dy = [1, -1, -1, 0, 1, -1,  0,  1]
            while True:
                Y_MAX, X_MAX = map(int, input[offset].split())
                if Y_MAX == 0 and X_MAX == 0:
                    break
                offset += 1
                visited = [[False] * Y_MAX for _ in range(X_MAX)]
                maps = []
                for x in range(X_MAX):
                    maps.append(list(map(int, input[offset + x].split())))
                offset += X_MAX
                answer = 0

                def bfs(x0, y0):
                    nonlocal visited, maps, dx, dy, Y_MAX, X_MAX, LAND
                    q = deque([(x0, y0)])
                    while q:
                        x, y = q.popleft()
                        if not visited[x][y]:
                            visited[x][y] = True
                            for i in range(8):
                                nx, ny = x + dx[i], y + dy[i]
                                if nx >= X_MAX or ny >= Y_MAX or nx < 0 or ny < 0:
                                    continue
                                if not visited[nx][ny] and maps[nx][ny] == LAND:
                                    q.append((nx, ny))
                lands = []
                for x in range(X_MAX):
                    for y in range(Y_MAX):
                        if maps[x][y] == LAND:
                            lands.append((x, y))
                if Y_MAX == X_MAX == 1:
                    # dot shape
                    answer = maps[0][0]
                else:
                    for x, y in lands:
                        if not visited[x][y]:
                            bfs(x, y)
                            answer += 1
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
            inputs.append(read_file(f"섬의 개수/input{i}.txt"))
            answers.extend(map(int, read_file(f"섬의 개수/output{i}.txt")))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()