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
        for ci in inputs:
            """
            dp[i] = max(dp[i-weight] + value, dp[i]) for weight, value in item for item in items
            """
            # your code here
            i_max, w_max = map(int, ci[0].split())
            dp = [0] * (w_max + 1)
            items = []
            for i in range(i_max):
                items.append(list(map(int, ci[1+i].split())))
            for item in items:
                weight, value = item
                for i in range(w_max, weight-1, -1):
                    dp[i] = max(dp[i - weight] + value, dp[i])
            answer = dp[-1]
            answers.append(answer)
        return answers
    except Exception:
        print(f"===========================================================================")
        print(f"Failed in the case below")
        print(f"input: {ci}")
        exc_info = sys.exc_info()
        print_exception(*exc_info)
        print(f"===========================================================================")
        del exc_info
class TestCases(unittest.TestCase):
    def test_input_txt(self):
        inputs, answers = [], []
        for i in range(1, 4 + 1):
            inputs.append(read_file(f"평범한 배낭/input{i}.txt"))
            answers.append(int(read_file(f"평범한 배낭/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()