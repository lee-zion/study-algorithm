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

def main(inputs):
    answers = []
    try:
        for input in inputs:
            # your code here
            n = int(input[0])
            k = math.log2(n / 3)
            S = pow(3, k)
            answer = [[""] * n for _ in range(n)]

            def print_star(x, y):
                nonlocal answer
                answer[x][y+2] = "*"
                answer[x+1][y+1] = "*"
                answer[x+1][y+3] = "*"
                for dy in range(5):
                    answer[x+2][y+dy] = "*"
            
            def get_locs():
                nonlocal n, k, S
                iter = 0
                locs = []
                lx, ly = 0, S
                for depth in range(S):
                    lx, ly = 3*depth, ly
                    locs.append((lx, ly))

                return locs
            
            locs = get_locs()

            for lx, ly in locs:
                print_star(lx, ly)
            offset = 0
            for i in range(k + 1):
                print_star(offset)
                offset += i
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
        for i in range(1, 1 + 1):
            inputs.append(read_file(f"별 찍기 - 11/input{i}.txt"))
            answers.append(int(read_file(f"별 찍기 - 11/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()