import unittest
from traceback import print_exception
import sys, itertools

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
            # math.comb vs itertools.combinations vs itertools.permutations
            n, m = map(int, input[0].split())
            # submitted
            # num = map(int, input[1].split())
            # answer = [' '.join(map(str, i)) for i in sorted(itertools.permutations(num, m))]
            # enhanced by reference https://www.acmicpc.net/source/52647478
            num = input[1].split()
            answer = [' '.join(i) for i in itertools.permutations(sorted(num, key=int), m)]
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
        for i in range(1, 4 + 1):
            inputs.append(read_file(f"e1b29736e27d8dc99d0f01ace419fcfe9cc51ee8/input{i}.txt"))
            answers.append(read_file(f"e1b29736e27d8dc99d0f01ace419fcfe9cc51ee8/output{i}.txt"))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()