import unittest
from traceback import print_exception
import sys, math
from decimal import setcontext, Context, Decimal, ROUND_CEILING
setcontext(Context(prec=12))
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
            den, num = map(Decimal, input[0].split())
            b34 = (1 - num / den * 10**2 % 1) / 100
            det = (1 - b34) * den - num
            answer = (b34 * den**2 / det).to_integral_exact(rounding=ROUND_CEILING) if det > 0 else -1
            answers.append(answer)
            # answers.append(math.ceil(answer))
            # det = 99 * den - 100 * num
            # answers.append(math.ceil(den**2 / det) if det > 0 else -1)
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
        for i in range(1, 6 + 1):
            inputs.append(read_file(f"게임/input{i}.txt"))
            answers.append(int(read_file(f"게임/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()