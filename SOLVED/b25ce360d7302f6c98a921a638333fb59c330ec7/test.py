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
            n, m = map(int, input[0].split())
            num = [str(i) for i in range(1, n+1)]
            # math.comb vs itertools.combinations vs itertools.permutations
            answer = [' '.join(i) for i in itertools.combinations(num, m)]
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
        for i in range(1, 3 + 1):
            inputs.append(read_file(f"b25ce360d7302f6c98a921a638333fb59c330ec7/input{i}.txt"))
            answers.append(read_file(f"b25ce360d7302f6c98a921a638333fb59c330ec7/output{i}.txt"))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()