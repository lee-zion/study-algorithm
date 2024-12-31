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
            """
            dp[i] = number of way to represent "i"
            Possible last term of dp[i] must be in [1, 2, 3]
            If dp[i] ends with 1, dp[i] = dp[i-1]
            dp[i-1] = number of way to represent "i-1"
            
            If dp[i] ends with 2, dp[i] = dp[i-2]
            dp[i-2] = number of way to represent "i-2"
            
            If dp[i] ends with 3, dp[i] = dp[i-3]
            dp[i-3] = number of way to represent "i-3"

            Therefore, dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

            dp[0] = 1
            dp[1] = 1
            dp[2] = 2
            dp[3] = 4 = 1+1+2
            dp[4] = 7 = 1+2+4
            dp[5] = ...
            """
            n = int(input[0])
            nums = list(map(int, input[1:]))
            dp = [0 for _ in range(max(max(nums) + 1, 3))]
            dp[0] = 1
            dp[1] = 1
            dp[2] = 2
            for num in nums:
                if num < 3 or dp[num] > 0:
                    return dp[num]
                for i in range(3, num + 1):
                    if dp[i] == 0:
                        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
                answer = dp[num]
                answers.append(str(answer))
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
            inputs.append(read_file(f"1, 2, 3 더하기/input{i}.txt"))
            answers.append(read_file(f"1, 2, 3 더하기/output{i}.txt"))
        self.assertEqual(main(inputs), answers[0])


if __name__ == '__main__':
    unittest.main()