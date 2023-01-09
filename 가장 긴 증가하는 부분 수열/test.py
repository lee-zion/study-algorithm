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
    try:
        for input in inputs:
            # your code here
            """
            Longest Increasing Subsequence
            https://seungkwan.tistory.com/8
            """
            n = int(input[0])
            nums = list(map(int, input[1].split()))
            dp = [0] * n
            dp[0] = nums[0]
            largests = [nums[0]]
            answers = [1]
            for ni, new in enumerate(nums[1:]):
                for ci, largest in enumerate(largests):
                    if new >= largest:
                        largest = new
                        dp[ni] = largest
                        answers[ci] += 1
                    else:
                        largests.append(new)
                        dp[ni] = new
                        answers.append(answers[ci] + 1)
            print(answers)
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
            inputs.append(read_file(f"가장 긴 증가하는 부분 수열/input{i}.txt"))
            answers.append(int(read_file(f"가장 긴 증가하는 부분 수열/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()