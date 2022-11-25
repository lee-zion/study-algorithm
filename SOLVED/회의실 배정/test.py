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
            meetings = None
            n = int(input[0])
            meetings = [list(map(int, input[1+j].split())) for j in range(n)]
            visited = [False] * n

            # Greedy
            answer = 1
            meetings = sorted(meetings, key = lambda x: (x[1], x[0]))
            begin_now, end_now = meetings[0]
            for begin_new, end_new in meetings[1:]:
                if begin_new >= end_now:
                    end_now = end_new
                    answer += 1
            # DFS: Timeout
            # meetings = sorted(meetings, key = lambda x: (x[1], x[0]))
            # answer = 0
            # def dfs(time, i_time, is_empty, temp):
            #     nonlocal meetings, visited, answer
            #     if is_empty:
            #         for i in range(i_time, n):
            #             begin, end = meetings[i]
            #             if time <= begin and not visited[i]:
            #                 visited[i] = True
            #                 dfs(end, i, True, temp + 1)
            #                 visited[i] = False
            #         answer = max(answer, temp)
            # dfs(0, 0, True, 0)
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
        for i in range(1, 3 + 1):
            inputs.append(read_file(f"회의실 배정/input{i}.txt"))
            answers.append(read_file(f"회의실 배정/output{i}.txt")[0])
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()