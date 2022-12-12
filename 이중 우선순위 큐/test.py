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
            offset = 0
            T = int(input[0])
            for t in range(T):
                heap_pos, heap_neg = [], []
                K = int(input[1+t+offset])
                for k in range(1, K+1):
                    oper, num = input[1+t+offset+k].split()
                    num = int(num)
                    if oper == "I":
                        if num > 0:
                            # max heap
                            heappush(heap_pos, -num)
                        else:
                            # max heap
                            heappush(heap_neg, -num)
                    elif oper == "D":
                        if num > 0:
                            # delete max
                            if heap_pos:
                                heappop(heap_pos)
                            elif heap_neg:
                                heappop(heap_neg)
                        else:
                            # delete min
                            if heap_neg:
                                heappop(heap_neg)
                            elif heap_pos:
                                heappop(heap_pos)
                offset += K
                heap = heapify(heap_pos + heap_neg)
                print(heap)
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
            inputs.append(read_file(f"이중 우선순위 큐/input{i}.txt"))
            read_file(f"이중 우선순위 큐/output{i}.txt")
        self.assertEqual(main(inputs), answers[0])


if __name__ == '__main__':
    unittest.main()