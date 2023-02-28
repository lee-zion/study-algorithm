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
            snow = list(map(int, input[1].split()))
            for i in range(n):
                allowed = 2*i + 1
                if snow[i] > allowed:
                    if i != n - 1:
                        snow[i+1] += snow[i] - allowed
                        snow[i] = allowed
                    else:
                        snow[i] = allowed
            answer = " ".join(map(str, snow))
            answers.append([answer])
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
        for i in range(1, 4 + 1):
            inputs.append(read_file(f"software-maestro/1/input{i}.txt"))
            answers.append(read_file(f"software-maestro/1/output{i}.txt"))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()