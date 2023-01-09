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
            dp = [[0] * 2 for _ in range(n+1)]
            IDX, VAL = 0, 1
            dp[i][IDX] = 0에서 시작해 숫자 i를 표현하는데 필요한 최소 연산 횟수
            dp[i][VAL] = ???
            """
            target = int(input[0])
            IDX, VAL = 0, 1
            dp = [[0] * 2 for _ in range(target+1)]
            # explicit is better than implicit
            # dp[0][IDX] = 0
            # dp[0][VAL] = 0
            for i in range(2, target+1):
                dp[i][IDX] = dp[i-1][IDX] + 1
                dp[i][VAL] = i - 1
                if i % 2 == 0:
                    # dp[i] = min(dp[i], dp[i // 2] + 1)
                    if dp[i][IDX] > dp[i // 2][IDX] + 1:
                        dp[i][IDX] = dp[i // 2][IDX] + 1
                        dp[i][VAL] = i // 2
                if i % 3 == 0:
                    # dp[i] = min(dp[i], dp[i // 3] + 1)
                    if dp[i][IDX] > dp[i // 3][IDX] + 1:
                        dp[i][IDX] = dp[i // 3][IDX] + 1
                        dp[i][VAL] = i // 3
            trace = [target]
            idx = -1
            while dp[idx][VAL]:
                trace.append(dp[idx][VAL])
                idx = dp[idx][VAL]
            answer = [str(dp[-1][IDX]), " ".join(map(str, trace))]
            # answer = [str(dp[-1][VAL]), " ".join(map(str, nums))]
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
        for i in range(2, 2 + 1):
            inputs.append(read_file(f"1로 만들기 2/input{i}.txt"))
            answers.append(read_file(f"1로 만들기 2/output{i}.txt"))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()