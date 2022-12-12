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
            answer = 0
            n, k = map(int, input[0].split())
            items = []
            for i in range(n):
                items.append(list(map(int, input[1+i].split())))

            # DP 점화식
            # 

            # def dfs(curr, weight, value):
            #     nonlocal visited, items, k, answer
            #     if weight <= k:
            #         answer = max(answer, value)
            #         for adj in range(n):
            #             if not visited[adj]:
            #                 visited[adj] = True
            #                 w, v = items[adj]
            #                 dfs(curr, weight + w, value + v)
            #                 visited[adj] = False
            # for begin in range(n):
            #     visited = [False] * n
            #     visited[begin] = True
            #     w, v = items[begin]
            #     dfs(begin, w, v)
            
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
            inputs.append(read_file(f"평범한 배낭/input{i}.txt"))
            answers.append(int(read_file(f"평범한 배낭/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()