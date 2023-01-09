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
            n, begin = map(int, input[0].split())
            heap = []
            for i in range(n):
                start, interval, n_bus = map(int, input[1+i].split())
                for ib in range(n_bus):
                    begin_bus = start + interval*ib
                    if begin <= begin_bus:
                        heappush(heap, begin_bus)
            # print(heap)
            answer = heappop(heap) - begin if heap else -1
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
        for i in range(1, 5 + 1):
            inputs.append(read_file(f"캠프가는 영식/input{i}.txt"))
            answers.append(int(read_file(f"캠프가는 영식/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()