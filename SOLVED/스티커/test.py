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
            dp: (3 x n) array

            dp[i][0] = max(s[i][0] + dp[i-1][1], s[i][0] + dp[i-2][2])
            """
            FIRST, SECOND, LEAVE = 0, 1, 2
            n_test = int(input[0])
            for i_test in range(n_test):
                n = int(input[1 + 3*i_test])
                sticker = []
                dp = [[0] * n for _ in range(3)]
                for i in range(2):
                    sticker.append(list(map(int, input[2 + 3*i_test + i].split())))
                    dp[i][0] = sticker[i][0]
                for i in range(1, n):
                    dp[FIRST][i] = max(dp[SECOND][i-1] + sticker[FIRST][i], dp[LEAVE][i-1] + sticker[FIRST][i])
                    dp[SECOND][i] = max(dp[FIRST][i-1] + sticker[SECOND][i], dp[LEAVE][i-1] + sticker[SECOND][i])
                    dp[LEAVE][i] = max(dp[FIRST][i-1], dp[SECOND][i-1])

                answer = max(dp[i][n-1] for i in range(3))
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
            inputs.append(read_file(f"스티커/input{i}.txt"))
            answers.append(read_file(f"스티커/output{i}.txt"))
        self.assertEqual([main(inputs)], answers)


if __name__ == '__main__':
    unittest.main()