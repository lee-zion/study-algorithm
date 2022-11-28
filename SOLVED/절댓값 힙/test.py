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
            answer = 0
            h = []
            for i in range(n):
                m = int(input[1+i])
                if m < 0:
                    heappush(h, (-m, -1))
                elif m > 0:
                    heappush(h, (m, 1))
                else:
                    try:
                        num, sign = heappop(h)
                        answer = num*sign
                    except IndexError:
                        answer = 0
                    finally:
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
        for i in range(1, 1 + 1):
            inputs.append(read_file(f"절댓값 힙/input{i}.txt"))
            answers = read_file(f"절댓값 힙/output{i}.txt")
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()