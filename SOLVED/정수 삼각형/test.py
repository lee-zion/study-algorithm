import unittest
from traceback import print_exception
import sys
from collections import deque


def read_file(filename):
    file = open(filename, "r")
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret


class BinaryTree:
    def __init__(self) -> None:
        self.value = None
        self.parent = None
        self.left = None
        self.right = None

    def insert(self, value, parent, left, right):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

def main(inputs):
    answers = []
    try:
        for input in inputs:
            h = int(input[0])
            a = []
            for depth in range(h):
                a.append(list(map(int, input[1 + depth].split())))
            
            # DP 점화식
            # dp[i+1] = dp[i] + max(a[i], a[i+1])
            dp = [0] * h
            dp[0] = a[0][0]
            for depth in range(1, h):
                temp = [0] * h
                for i, v in enumerate(a[depth]):
                    if i == 0:
                        temp[i] = dp[i] + v
                    elif i == len(a[depth]) - 1:
                        temp[i] = dp[i-1] + v
                    else:
                        temp[i] = v + max(dp[i], dp[i-1])
                dp = temp
            answer = max(dp)

            # def dfs(depth, acc, i_prev):
            #     nonlocal h, answer, graph
            #     if depth == h:
            #         answer = max(answer, acc)
            #     else:
            #         dfs(depth + 1, acc + graph[depth + 1][i_prev])
            #         dfs(depth + 1, acc + graph[depth + 1][i_prev + 1])

            # dfs(0, 0, graph[0][0])
            answers.append(answer)
        return answers
    except Exception:
        print(
            f"==========================================================================="
        )
        print(f"Failed in the case below")
        print(f"input: {input}")
        exc_info = sys.exc_info()
        print_exception(*exc_info)
        print(
            f"==========================================================================="
        )
        del exc_info


class TestCases(unittest.TestCase):
    def test_input_txt(self):
        inputs, answers = [], []
        for i in range(1, 1 + 1):
            inputs.append(read_file(f"정수 삼각형/input{i}.txt"))
            answers.append(int(read_file(f"정수 삼각형/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == "__main__":
    unittest.main()
