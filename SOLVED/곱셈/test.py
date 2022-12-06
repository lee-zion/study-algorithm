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
            # exponential using divide-and-conquer
            # or exponential by squaring
            def expmod(base, exp, mod):
                if exp == 0:
                    return 1
                if exp == 1:
                    return base % mod
                else:
                    half = expmod(base, exp // 2, mod) % mod
                    if exp % 2 == 0:
                        return pow(half, 2) % mod
                    else:
                        return pow(half, 2) % mod * base % mod
            a, b, c = map(int, input[0].split())
            a, b, c = 2_147_483_647, 2_147_483_647, 5
            answer = expmod(a, b, c)
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
        for i in range(1, 1 + 1):
            inputs.append(read_file(f"곱셈/input{i}.txt"))
            answers.append(int(read_file(f"곱셈/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()