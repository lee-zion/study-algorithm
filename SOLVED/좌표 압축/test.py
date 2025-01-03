import unittest
from traceback import print_exception
import sys
from collections import Counter

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
            갯수는 100만개, 값의 범위는 10**9

            basic)
            element x의 sorted에서의 위치 인덱스 = x보다 작은 element의 수

            example)
            list: 2 4 -10 4 -9
            sort: -10 -9 2 4 4

            2의 sorted에서의 index = 2 -> 더 작은 수 2개
            4의 sorted에서의 index = 3 -> 더 작은 수 3개
            -10의 sorted에서의 index = 0 -> 제일 작음

            additional)
            i보다 작은 값의 위치를 cache해서 매번 찾지 않도록 최적화
            """
            n = int(input[0])
            x_list = list(map(int, input[1].split()))
            x_list_sorted = sorted(list(set(x_list)))
            answer = [0] * n
            cache = {}
            for i, x in enumerate(x_list):
                if x in cache:
                    answer[i] = cache[x]
                    continue
                answer[i] = x_list_sorted.index(x)
                cache[x] = answer[i]

            answers.append([" ".join(map(str, answer))])
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
            inputs.append(read_file(f"좌표 압축/input{i}.txt"))
            answers.append(read_file(f"좌표 압축/output{i}.txt"))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()