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
            answer = 0
            num_str = input[0]
            if int(num_str) < 110:
                answer = min(99, int(num_str))
            else:
                answer = 99
                for num in range(111, min(1000, int(num_str) + 1)):
                    a_prev = num % 10
                    a_now = num // 10 % 10
                    d = a_now - a_prev
                    a_prev = a_now
                    for i in range(2, len(str(num))):
                        a_now = num // 10**(i) % 10
                        if a_now - a_prev != d:
                            break
                        answer += 1
                        a_prev = a_now
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
        for i in range(1, 5 + 1):
            inputs.append(read_file(f"한수/input{i}.txt"))
            answers.append(int(read_file(f"한수/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()