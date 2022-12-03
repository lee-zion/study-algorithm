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
            T = int(input[0])
            for t in range(T):
                r, S = input[1+t].split()
                answer = ""
                for i, s in enumerate(S):
                    answer += S[i] * int(r)
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
            inputs.append(read_file(f"문자열 반복/input{i}.txt"))
            answers.append(read_file(f"문자열 반복/output{i}.txt"))
        self.assertEqual(main(inputs), answers[0])


if __name__ == '__main__':
    unittest.main()