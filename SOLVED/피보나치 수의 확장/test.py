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
            n = int(input[0])
            
            if n > 0 or (n < 0 and n%2 == 1):
                sign = 1
            elif n == 0:
                sign = 0
            else:
                sign = -1
            
            nabs = abs(n)
            dp = [0] * (nabs + 1)
            if nabs >= 1:
                dp[1] = 1
            if nabs >= 2:
                dp[2] = 1
            for ni in range(3, max(3, nabs+1)):
                dp[ni] = (dp[ni - 1] + dp[ni - 2]) % 10**9
            answer = dp[nabs] if n != 0 else 0
            answers.append([sign, answer])
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
            inputs.append(read_file(f"피보나치 수의 확장/input{i}.txt"))
            answers.append(list(map(int, read_file(f"피보나치 수의 확장/output{i}.txt"))))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()