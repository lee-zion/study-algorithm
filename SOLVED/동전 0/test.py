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
            n k
            dp
                  0   1    ...                    n-2   n-1
                  1   5   10 50 100 500 1000 5000 10000 50000
            1     K-1 K-5
            2     K-2 
            ...       
            K     0   
            
            dp[i][j] === j번째 동전 i개를 썼을 때의 가치

            dp[j1][0] + dp[j2][1] + dp[j3][2] + ... + dp[jk][n-1] = K를 만족하는 가장 작은 J=j1 + j2 + ... + jk를 구하라
            greedy approach

            dp[j1][0] + ... + dp[j_k-1][n-2] = K-dp[n-1]*MAX_jk
            """
            n, k = map(int, input[0].split())
            coins = []
            for i in range(1, n+1):
                coins.append(int(input[i]))
            answer = 0
            while k != 0:
                coin = coins.pop()
                if k < coin:
                    continue
                q, r = divmod(k, coin)
                answer += q
                k = r
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
            inputs.append(read_file(f"동전 0/input{i}.txt"))
            answers.append(read_file(f"동전 0/output{i}.txt"))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()