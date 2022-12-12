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
            X_MAX, Y_MAX = map(int, input[0].split())
            graph = []
            for i in range(X_MAX):
                graph.append(list(map(int, input[1+i].split())))
            answer = 0

            EMPTY, WALL, VIRUS = 0, 1, 2
            propagatables = []
            for x in range(X_MAX):
                for y in range(Y_MAX):
                    if graph[x][y] == VIRUS:
                        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
                        is_propagatable = True
                        for i in range(4):
                            vx, vy = x + dx[i], y + dy[i]
                            if vx < 0 or vy < 0 or vx >= X_MAX or vy >= Y_MAX:
                                continue
                            if graph[vx][vy] == EMPTY:
                                is_propagatable = True
                                # 어디를 막아야 (vx, vy)가 퍼지지 않게 할 수 있을까? 최소 0개(이미 막힘), 최대 4개의 벽이 필요
                                break
                        if is_propagatable:
                            # (x,y) should be blocked
                            # from (x,y), find from its nearest empty space
                            propagatables.append((x, y))
            # 어디를 막아야 (vx, vy)가 퍼지지 않게 할 수 있을까? 최소 0개(이미 막힘), 최대 4개의 벽이 필요
            for vx, vy in propagatables:
                dist = 1
                visited = []
                q = deque([vx, vy])
                while q:
                    vx, vy = q.popleft()
                    visited.append((vx, vy))
                    for i in range(dist):
                        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
                        for i in range(4):
                            vx, vy = vx + dx[i], vy + dy[i]
                            if vx < 0 or vy < 0 or vx >= X_MAX or vy >= Y_MAX or (vx, vy) in visited:
                                continue


                print(vx, vy)
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
        for i in range(1, 3 + 1):
            inputs.append(read_file(f"연구소/input{i}.txt"))
            answers.append(int(read_file(f"연구소/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()