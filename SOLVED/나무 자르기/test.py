import unittest
from traceback import print_exception
import sys
import math

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
            sum([max(0, h[i] - x) for i in range(n)]) >= M을 만족하는 정수 x의 최대값을 구하라.
            단, h: List[int]이며 sum(h) >= M을 항상 만족한다.

            h의 평균을 avg라고 할 경우, avg * n = sum(h)이다.
            
            1) bisect

            1-1) initial guess?

            example)
            0 100 -> M = m일 경우 x=100-m의 높이로 설정해야함
            """
            n, m = map(int, input[0].split())
            trees = list(map(int, input[1].split()))
            trees.sort()
            left, right = 0, max(trees)
            answer = right
            while left <= right:
                cut = 0
                mid = (left + right) // 2
                for tree in trees:
                    cut += max(0, tree - mid)
                if cut >= m:
                    answer = mid
                    left = mid + 1
                else:
                    right = mid - 1
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
        for i in range(1, 2 + 1):
            inputs.append(read_file(f"나무 자르기/input{i}.txt"))
            answers.append(int(read_file(f"나무 자르기/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()