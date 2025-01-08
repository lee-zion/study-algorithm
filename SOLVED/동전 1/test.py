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
            """
            dp[i] = dp[i] + dp[i - coin] for coin in coins
            """
            # your code here
            n, target = map(int, input[0].split())
            coins = []
            dp = [0] * (target + 1)
            dp[0] = 1
            for i in range(n):
                coins.append(int(input[1+i]))
            for coin in coins:
                for i in range(coin, target + 1):
                    dp[i] += dp[i - coin]
            answer = dp[target]
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
            inputs.append(read_file(f"동전 1/input{i}.txt"))
            answers.append(int(read_file(f"동전 1/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()