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
            Let L[i][j] = maximum length of LCS

            if x[i] == y[j], we can increase LCS by 1
            L[i][j] = L[i-1][j-1] + 1

            if x[i] != y[j], we choose maximum LCS from previous candidates:
            L[i][j] = max(L[i][j-1], L[i-1][j])
            """
            x, y = input[0], input[1]
            answer = 0

            xm, ym = len(x), len(y)
            dp = [[0] * (ym+1) for _ in range(xm+1)]

            for i in range(xm):
                for j in range(ym):
                    if x[i] == y[j]:
                        dp[i+1][j+1] = dp[i][j] + 1
                    else:
                        dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
            
            def get_lcs_from_dp(dp):
                xm, ym = len(dp), len(dp[0])
            answer = dp[xm][ym]
            answers.append([str(answer)])
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
            inputs.append(read_file(f"LCS/input{i}.txt"))
            answers.append(read_file(f"LCS/output{i}.txt"))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()