import unittest
from traceback import print_exception
import sys

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
            n, m = map(int, input[0].split())
            graph = [[0]*m for _ in range(n)]
            for x in range(n):
                for y in range(m):
                    graph[x][y] = input[x + 1][y]
            
            pool = set()
            # TODO
            # cdx, cdy = x + cx*dx, y + cy*dy
            # cx in range([-n, n])
            # cy in range([-m, m])
            # for given cdx, cdy:
            # temp = ""
            #   if cdx, cdy is valid:
            #       temp += graph[cdx][cdy]
            #   else:
            #       break
            for x in range(n):
                for y in range(m):
                    for dx in range(n):
                        plus, minus = "", ""
                        for dy in range(m):
                            px, py = x+dx, y+dy
                            nx, ny = x-dx, y-dy
                            if px < n and py < m:
                                plus += graph[px][py]
                            if nx >= 0 and ny >= 0:
                                minus += graph[nx][ny]
                            if px == 0 and py == 0:
                                break
                        pool.add(plus)
                        pool.add(minus)
            answer = True
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
        for i in range(1, 6 + 1):
            inputs.append(read_file(f"제곱수 찾기/input{i}.txt"))
            answers.append(read_file(f"제곱수 찾기/output{i}.txt")[0])
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()