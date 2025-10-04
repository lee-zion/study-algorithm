import unittest
from traceback import print_exception
import sys
from collections import deque

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
            dp[i] = 수빈이가 점 i까지 도달하는데 걸리는 최소 시간

            dp[i//2] = min(dp[i], dp[i//2])
            """
            n, k = map(int, input[0].split())
            MAX = 100_000
            INIT = MAX + 1
            dp = [INIT] * INIT
            q = deque()
            q.append((n, 0))
            answer = INIT
            while q:
                curr, time = q.popleft()
                if curr >= k:
                    answer = min(answer, time + curr - k)
                    continue
                dp[curr] = time
                i = 2
                while curr > 0:
                    if dp[curr*i] > dp[curr]:
                        dp[curr*i] = min(dp[curr*i], dp[curr])
                        q.append((curr*i, time))
                    i *= 2
                    if curr*i > MAX:
                        break
                if curr >= 1 and dp[curr - 1] > dp[curr]:
                    dp[curr - 1] = time + 1
                    q.append((curr-1, time + 1))
                if curr <= MAX and dp[curr + 1] > dp[curr]:
                    dp[curr + 1] = time + 1
                    q.append((curr+1, time + 1))
            answer = dp[k]
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
        for i in range(1, 1 + 1):
            inputs.append(read_file(f"숨바꼭질 3/input{i}.txt"))
            answers.append(read_file(f"숨바꼭질 3/output{i}.txt"))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()