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
            orders = list(map(int, input[0].split()))[:-1]
            # prev를 curr로 옮길 경우 필요한 힘 계산
            # prev == 0 인 경우, 첫 움직임으로 간주
            # curr == 0 인 경우, 마지막 움직임으로 간주
            # prev == curr 인 경우, 이상값(INF) 반환
            def move(prev, curr):
                # 0 -> 1,2,3,4 = 2
                # 1 -> 1 = 1
                # 2 -> 2 = 1
                # 3 -> 3 = 1
                # 4 -> 4 = 1
                # 1 -> 3 = 4
                # 3 -> 1 = 4
                # 2 -> 4 = 4
                # 4 -> 2 = 4
                # else -> else = 3
                if prev == 0:
                    # initial
                    return 2
                diff = (prev - curr) % 4
                if diff == 0:
                    return 1
                if diff == 2:
                    return 4
                return 3
            DP_INIT = -1
            dp = [[[DP_INIT] * 10**5 for _ in range(5)] for _ in range(5)]
            def solve_dp(l, r, n):
                nonlocal orders, dp, DP_INIT
                if n == len(orders):
                    return 0

                if dp[l][r][n] != DP_INIT:
                    return dp[l][r][n]
                
                dp[l][r][n] = min(move(l, orders[n]) + solve_dp(orders[n], r, n + 1), move(r, orders[n]) + solve_dp(l, orders[n], n + 1))

                return dp[l][r][n]

            def solve_dfs(l, r, n, lpath, rpath, lacc, racc):
                nonlocal orders

                print(f"lpath: {lpath}")
                print(f"rpath: {rpath}")

                if n == len(orders):
                    print(f"left : {lacc}")
                    print(f"right: {racc}")
                    return 0
                
                return min(move(l, orders[n]) + solve_dfs(orders[n], r, n + 1, lpath + str(orders[n]), rpath, move(l, orders[n]) + lacc, racc), move(r, orders[n]) + solve_dfs(l, orders[n], n + 1, lpath, rpath + str(orders[n]), lacc, move(r, orders[n]) + racc))
            
            answer = solve_dp(0, 0, 0)
            # answer = solve_dfs(0, 0, 0, "0", "0", 0, 0)
            # 0 → 1 → 2 → 2 / 0 -> 4
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
            inputs.append(read_file(f"Dance Dance Revolution/input{i}.txt"))
            answers.append(int(read_file(f"Dance Dance Revolution/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()