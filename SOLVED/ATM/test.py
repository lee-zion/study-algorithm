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
            prefix sum
            total time required for n people given a[1], a[2], ..., a[n]
            n*a[0] + (n-1)a[1] + ... + 2a[n-1] + a[n]
            minimum => sort in ascending order
            """
            n = int(input[0])
            nums = sorted(list(map(int, input[1].strip().split())))
            idxs = [i for i in range(n, 0, -1)]
            answer = sum(list(map(lambda a,b: a*b, nums, idxs)))
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
        for i in range(1, 1 + 3):
            inputs.append(read_file(f"ATM/input{i}.txt"))
            answers.append(int(read_file(f"ATM/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()