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
            n = int(input[0])
            nnnnn = 5*n
            nnnn = 4*n
            nnn = 3*n
            answer = []
            for i in range(nnnnn):
                if i < n or i >= nnnn:
                    answer.append("@"*nnnnn)
                else:
                    answer.append("@"*n + " "*nnn + "@"*n)
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
            inputs.append(read_file(f"골뱅이 찍기 - ㅁ/input{i}.txt"))
            answers.append(read_file(f"골뱅이 찍기 - ㅁ/output{i}.txt"))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()