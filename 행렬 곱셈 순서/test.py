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
            n = int(input[0])
            matrices = []
            dp = [[0] * (n+1) for _ in range(n+1)]
            # (r_1, c_1) x (r_2, c_2) x ... x (r_n, c_n)
            # c_i = r_i+1
            # (r_1, c_1) x (r_2, c_2) = (r_1, c_2) + r_1*c_1*c_2
            # n-1번 연산
            # dp[x][y] = x번째 행렬부터 y번째 행렬까지 곱하는 경우 필요한 곱셈 연산의 수
            for i in range(n):
                r, c = map(int, input[1+i].split())
                matrices.append((r, c))
                dp[i+1][i+1] = r*c
            for 
            answer = True
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
            inputs.append(read_file(f"행렬 곱셈 순서/input{i}.txt"))
            answers.append(int(read_file(f"행렬 곱셈 순서/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()