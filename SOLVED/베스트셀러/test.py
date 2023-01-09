import unittest
from traceback import print_exception
from collections import defaultdict
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
            sell = {}
            for i in range(n):
                title = input[1+i]
                if title in sell:
                    sell[title] += 1
                else:
                    sell[title] = 1
            answer = sorted(sorted(sell.items()), key=lambda x: x[1], reverse=True)
            answers.append([answer[0][0]])

            n = int(input[0])
            sell = defaultdict(int)
            for i in range(n):
                title = input[1+i]
                sell[title] += 1
            answer = sorted(sorted(sell.items()), key=lambda x:x[1], reverse=True)
            answers.append([answer[0][0]])
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
        for i in range(1, 5 + 1):
            inputs.append(read_file(f"베스트셀러/input{i}.txt"))
            answers.append(read_file(f"베스트셀러/output{i}.txt"))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()