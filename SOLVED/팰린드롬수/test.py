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
            i = 0
            nums = []
            while True:
                num = input[i]
                if num == "0":
                    break
                nums.append(num)
                i += 1

            for num in nums:
                n = len(num)
                n2 = n // 2
                l, r = num[:n2], num[n2:] if n%2 == 0 else num[n2+1:][::-1]
                if l == r:
                    answers.append("yes")
                else:
                    answers.append("no")

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
            inputs.append(read_file(f"팰린드롬수/input{i}.txt"))
            answers.append(read_file(f"팰린드롬수/output{i}.txt"))
        self.assertEqual(main(inputs), answers[0])


if __name__ == '__main__':
    unittest.main()