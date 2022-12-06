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
            T = int(input[0])
            for it in range(T):
                answer = None
                x1, y1, r1, x2, y2, r2 = map(int, input[1+it].split())
                if x1 == x2 and y1 == y2:
                    answer = -1 if r1 == r2 else 0
                else:
                    # always r1 >= r2
                    if r2 > r1:
                        x1, y1, r1, x2, y2, r2 = x2, y2, r2, x1, y1, r1
                    d = math.sqrt(pow(abs(x1 - x2), 2) + pow(abs(y1 - y2), 2))
                    answer = 0 if d > r1 + r2 else 1 if d == r1 + r2 else 0 if d + r2 < r1 else 1 if r1 == r2 + d else 2
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
            inputs.append(read_file(f"터렛/input{i}.txt"))
            answers.append(list(map(int, read_file(f"터렛/output{i}.txt"))))
        self.assertEqual(main(inputs), answers[0])


if __name__ == '__main__':
    unittest.main()