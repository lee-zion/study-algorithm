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
            # a, b = map(int, input[0].split())
            # answer_true = a / b
            # answer, x = 0, 0.1
            # precision = 10**-10
            # while True:
            #     x = x * (2 - b * x)
            #     answer = x * a
            #     diff_abs = math.fabs(answer - answer_true)
            #     diff_rel = diff_abs / answer_true * 100
            #     if diff_abs <= precision or diff_rel <= precision:
            #         break
            # answers.append(answer)

            a, b = map(int, input[0].split())
            answers.append(a / b)
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
        for i in range(2, 2 + 1):
            inputs.append(read_file(f"A/B/input{i}.txt"))
            answers.append(float(read_file(f"A/B/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()