import unittest
from traceback import print_exception
import sys
import heapq

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
            n = int(input[0])
            nums = []
            for i in range(n):
                temp = int(input[1+i])
                if temp:
                    heapq.heappush(nums, temp)
                else:
                    if nums:
                        answers.append(heapq.heappop(nums))
                    else:
                        answers.append(0)
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
            inputs.append(read_file(f"최소 힙/input{i}.txt"))
            answers.append(read_file(f"최소 힙/output{i}.txt"))
        self.assertEqual(main(inputs), list(map(int, answers[0])))


if __name__ == '__main__':
    unittest.main()