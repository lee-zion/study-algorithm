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
            # consults = [0] * (n + 1)
            # for i in range(n):
            #     time, profit = map(int, input[1+i].split())
            #     consults[time] = profit
            consults = []
            for curr in range(n):
                time, profit = map(int, input[1+curr].split())
                consults.append((time, profit))
            dp = [0] * (n + 1)
            time, profit = consults[n-1]
            for curr in range(n-1, -1, -1):
                time, profit = consults[curr]
                if curr + time > n:
                    dp[curr] = dp[curr+1]
                else:
                    dp[curr] = max(dp[curr + 1], profit + dp[curr + time])
            # dp[x][y] == 
            # 아래 두 값중에 더 큰값으로 갱신이 이루어진다 
            # i번째 일을 할때의 이익 ( = i번째일의 이익 + i번째일을 하는데 걸리는시간후의 이익)  : cost[i]+dp[i+day[i]])
            # i번째 일을 건너뛰고 i+1번째 일을 할때의 이익 : dp[i+1]
            # 핵심 점화식 :   dp[i] = max(dp[i+1], cost[i]+dp[i+day[i]])
            answer = dp[0]
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
        for i in range(1, 4 + 1):
            inputs.append(read_file(f"퇴사/input{i}.txt"))
            answers.append(read_file(f"퇴사/output{i}.txt"))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()