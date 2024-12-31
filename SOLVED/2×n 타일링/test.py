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
            # your code here
            """
            if n >= 2:
                1) (2 x 1), 1EA -> (2 x n) -> (2 x n-1)
                2) (1 x 2), 2EA -> (2 x n) -> (2 x n-2)
            else:
                (2 x 1), 1EA

            f(1) = 1
            f(2) = 2
            f(3) = f(3-1) + f(3-2) = f(2) + f(1) = 3
            f(4) = f(4-1) + f(4-2) = f(3) + f(2) = 5
            f(5) = f(5-1) + f(5-2) = 8
            f(6) = 13
            f(7) = 21
            f(8) = 34
            f(9) = 55
            ...
            f(n) = {1 + f(n-1)} + {f(2) + f{n-2}}
            """
            n = int(input[0])
            if n < 3:
                answer = n
            else:
                answer = 0
                prev_prev_answer = 1
                prev_answer = 2
                for i in range(n-2):
                    answer = prev_answer + prev_prev_answer
                    prev_prev_answer = prev_answer
                    prev_answer = answer
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
            inputs.append(read_file(f"2×n 타일링/input{i}.txt"))
            answers.append(int(read_file(f"2×n 타일링/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()