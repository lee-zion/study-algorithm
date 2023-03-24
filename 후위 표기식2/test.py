import unittest
from traceback import print_exception
import sys
import string
from collections import deque

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
            """
            (b*c+a)-(d/e)
            2 3 1 4 5
            =
            7-0.8=6.2
            """
            # your code here
            n_var = int(input[0])
            equation = input[1]
            vals = []
            for i in range(n_var):
                vals.append(int(input[2+i]))
            
            def get_alphabet_idx(c):
                return vals[string.ascii_uppercase.find(c)]
            
            q = deque([])
            for s in equation:
                if s in ["+", "-", "*", "/"]:
                    a = q.pop()
                    b = q.pop()
                    c = eval(f"{b}{s}{a}")
                    q.append(c)
                else:
                    q.append(get_alphabet_idx(s))
            answer = q.pop()
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
        for i in range(1, 2 + 1):
            inputs.append(read_file(f"후위 표기식2/input{i}.txt"))
            answers.append(float(read_file(f"후위 표기식2/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()