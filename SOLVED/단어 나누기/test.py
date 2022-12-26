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
            given = input[0]
            answer = []
            l = len(given)
            for i in range(l-2):
                for j in range(i + 1, l-1):
                    s1, s2, s3 = given[:i+1], given[i+1:j+1], given[j+1:]
                    answer.append(s1[::-1] + s2[::-1] + s3[::-1])
            answers.append(sorted(answer)[0])
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
            inputs.append(read_file(f"단어 나누기/input{i}.txt"))
            answers.append(read_file(f"단어 나누기/output{i}.txt")[0])
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()