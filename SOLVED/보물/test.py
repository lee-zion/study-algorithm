import unittest
from traceback import print_exception
import sys
from heapq import heappush, heappop, heapify

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
            
            # a = sorted(list(map(int, input[1].split())))
            # b = sorted(list(map(int, input[2].split())]), reversed=True)
            # answer = 0
            # for i in range(n):
            #     answer += a[i] * b[i]
            
            a = list(map(int, input[1].split()))
            b = [-i for i in map(int, input[2].split())]

            heapify(a)
            heapify(b)
            answer = 0
            for i in range(n):
                answer -= heappop(a) * heappop(b)
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
        for i in range(1, 3 + 1):
            inputs.append(read_file(f"보물/input{i}.txt"))
            answers.append(int(read_file(f"보물/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()