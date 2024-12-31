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
            n, m
            a_1 a_2 ... a_n within [1, 1000]
            i_1 j_1
            i_2 j_2
            ...
            i_m j_m
            """
            n, m = map(int, input[0].split())
            nums = list(map(int, input[1].split()))
            prefix_sum = [0 for _ in range(n+1)]
            for i, num in enumerate(nums):
                prefix_sum[i+1] = prefix_sum[i] + num
            
            for pair in input[2:]:
                begin, end = map(int, pair.split())
                answer = prefix_sum[end] - prefix_sum[begin-1]
                answers.append(str(answer))
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
            inputs.append(read_file(f"구간 합 구하기 4/input{i}.txt"))
            answers.append(read_file(f"구간 합 구하기 4/output{i}.txt"))
        self.assertEqual(main(inputs), answers[0])


if __name__ == '__main__':
    unittest.main()