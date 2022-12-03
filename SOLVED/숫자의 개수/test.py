import unittest
from traceback import print_exception
import sys, string
from collections import Counter

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
            num = 1
            for i in range(3):
                num *= int(input[i])
            
            num_cnt = Counter()
            for s in str(num):
                num_cnt[s] += 1
            for i in string.digits:
                answers.append(num_cnt[i])
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
            inputs.append(read_file(f"숫자의 개수/input{i}.txt"))
            answers.append(list(map(int, read_file(f"숫자의 개수/output{i}.txt"))))
        self.assertEqual(main(inputs), answers[0])


if __name__ == '__main__':
    unittest.main()