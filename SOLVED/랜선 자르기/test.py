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
            n_have, n_needed = map(int, input[0].split())
            cables = []
            for i in range(n_have):
                cables.append(int(input[1+i]))
            bracket = [0, max(cables)]
            while bracket[1] - bracket[0] > 1e-04:
                mid = sum(bracket) / 2
                n_made = 0
                for cable in cables:
                    n_made += cable // mid
                if n_made < n_needed:
                    bracket[1] = mid
                else:
                    bracket[0] = mid
            answer = int(bracket[1])
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
            inputs.append(read_file(f"랜선 자르기/input{i}.txt"))
            answers.append(int(read_file(f"랜선 자르기/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()