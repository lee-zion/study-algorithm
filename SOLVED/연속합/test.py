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
            # dp[n] = max( sum(num[1:n]), sum(num[2:n]), ..., sum(num[n-1:n]) )
            n = int(input[0])
            num = list(map(int, input[1].split()))
            INF = num[0]
            dp = [INF] * n
            dp[0] = num[0]
            for i in range(1, n):
                dp[i] = max(dp[i-1] + num[i], num[i])

            answer = max(dp)
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
            inputs.append(read_file(f"연속합/input{i}.txt"))
            answers.append(int(read_file(f"연속합/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()