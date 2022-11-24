import unittest
from traceback import print_exception
import sys
from math import isqrt, pow

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
            graph = [input[1+i] for i in range(n)]
            answer = -1
            for x in range(n):
                for y in range(m):
                    for dx in range(-n, n):
                        for dy in range(-m, m):
                            nx, ny, temp = x, y, ""
                            while 0 <= nx < n and 0 <= ny < m:
                                temp += graph[nx][ny]
                                if dx == 0 and dy == 0:
                                    break
                                itemp = int(temp)
                                if pow(isqrt(itemp), 2) == itemp:
                                    answer = max(answer, itemp)
                                nx += dx
                                ny += dy
            answers.append(str(answer))
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