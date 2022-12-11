import unittest
from traceback import print_exception
import sys, string

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
            l = int(input[0])
            a = input[1]
            r, M = 31, 1234567891
            answer = 0

            alpha_dict = {char: value + 1 for value, char in enumerate(string.ascii_lowercase)}

            for i in range(l):
                answer += alpha_dict[a[i]] * pow(r, i)
                answer %= M
            
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
            inputs.append(read_file(f"Hashing/input{i}.txt"))
            answers.append(int(read_file(f"Hashing/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()