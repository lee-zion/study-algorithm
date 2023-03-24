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
            find maximum value of m that satisfies the equation below
            
            \max_{K}{V} \enspace \text{where } V = \sum_{i=0}^{m}{v_i} \text{ and } K \ge \sum_{i=0}^{m}{w_i}
            
            dp[w] = max(v1 + dp[w-w1], ..., vi + dp[w-wi])
            dp[0] = 0
            
            dp[i][j] :== maximum value with number of item = i, weight = j
            dp[i][j] = dp[i-1][j] if w_i > K
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w_i] + v_i)
            """
            # your code here
            I_MAX, W_MAX = map(int, ci[0].split())
            INIT = 0
            ROW, COL = I_MAX + 1, W_MAX + 1
            dp = [[INIT] * COL for _ in range(ROW)]
            candidate = []
            for i in range(1, I_MAX + 1):
                weight, value = map(int, ci[i].split())
                candidate.append((weight, value))
            
            WEIGHT, VALUE = 0, 1
            for i in range(I_MAX):
                for w in range(1, W_MAX):
                    if w < candidate[i][WEIGHT]:
                        dp[i][w] = dp[i-1][w]
                    else:
                        dp[i][w] = max(dp[i-1][w], dp[i-1][w-candidate[i][WEIGHT]] + candidate[i][VALUE])
            answer = dp[ROW-1][COL-1]
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
        for i in range(1, 2 + 1):
            inputs.append(read_file(f"평범한 배낭/input{i}.txt"))
            answers.append(int(read_file(f"평범한 배낭/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()