import unittest
from traceback import print_exception
import sys, math

def read_file(filename):
    file = open(filename, 'r')
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret

def read_file_with_space(filename):
    file = open(filename, 'r')
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip('\n')
    file.close()
    return ret

def main(inputs):
    answers = []
    try:
        for input in inputs:
            # your code here
            n = int(input[0])
            # n = 12 # 3 6 12 24 48
            k = int(math.log2(n / 3))
            S = pow(3, k)
            size = 3*pow(2, k+1) - 1
            graph = [[" "] * size for _ in range(n)]

            def print_star(depth, x, y):
                nonlocal graph
                if depth == 0:
                    print(f"x, y: {x}, {y}")
                    graph[x][y+2] = "*"
                    graph[x+1][y+1] = "*"
                    graph[x+1][y+3] = "*"
                    for dy in range(5):
                        graph[x+2][y+dy] = "*"
                else:
                    d = 3 * pow(2, depth - 1)
                    dx = [d, 0, d]
                    dy = [0, d, d*2]
                    for i in range(3):
                        print(f"depth: {depth}, x, y: {x}, {y}, dx, dy: {dx}, {dy}")
                        print_star(depth - 1, x + dx[i], y + dy[i])
            
            print_star(k, 0, 0)
            for i in range(n):
                print("".join(graph[i]))
                answers.append("".join(graph[i]))
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
            inputs.append(read_file(f"별 찍기 - 11/input{i}.txt"))
            answers.append(read_file_with_space(f"별 찍기 - 11/output{i}.txt"))

        for a in answers:
            for i in a:
                print(i)
        self.assertEqual(main(inputs), answers[0])


if __name__ == '__main__':
    unittest.main()