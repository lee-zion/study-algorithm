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
            """
            1) is idx in valid?
            -> If not, ignore it --> True
            2) is valid[idx] True or False?
            True -> top element is the new one. We need to delete it --> False
            False -> top element is already removed one. Ignore it --> True
            """
            offset = 0
            T = int(input[0])
            for t in range(T):
                heap_max, heap_min = [], []
                valid = dict()
                K = int(input[1+t+offset])
                idx = 0
                for k in range(1, K+1):
                    oper, num = input[1+t+offset+k].split()
                    num = int(num)

                    # if oper == 'I':
                    #     # 삽입 연산
                    #     heappush(heap_min, (num, idx))
                    #     heappush(heap_max, (-num, idx))
                    #     valid[idx] = True
                    #     idx += 1
                    # else:
                    #     # 삭제 연산
                    #     if num == 1:  # 최대값 삭제
                    #         while heap_max and not valid.get(heap_max[0][1], False):
                    #             heappop(heap_max)
                    #         if heap_max:
                    #             _, idx_visited = heappop(heap_max)
                    #             valid[idx_visited] = False
                    #     elif num == -1:  # 최소값 삭제
                    #         while heap_min and not valid.get(heap_min[0][1], False):
                    #             heappop(heap_min)
                    #         if heap_min:
                    #             _, idx_visited = heappop(heap_min)
                    #             valid[idx_visited] = False


                    if oper == "I":
                        heappush(heap_max, (-num, idx))
                        heappush(heap_min, (num, idx))
                        valid[idx] = True
                        idx += 1
                    elif oper == "D":
                        if num > 0:
                            # delete max
                            while heap_max and not valid.get(heap_max[0][1], False):
                                heappop(heap_max)
                            if heap_max:
                                val, idx_removed = heappop(heap_max)
                                valid[idx_removed] = False
                        else:
                            # delete min
                            while heap_min and not valid.get(heap_min[0][1], False):
                                heappop(heap_min)
                            if heap_min:
                                val, idx_removed = heappop(heap_min)
                                valid[idx_removed] = False
                offset += K
                while heap_max and not valid.get(heap_max[0][1], False):
                    heappop(heap_max)
                while heap_min and not valid.get(heap_min[0][1], False):
                    heappop(heap_min)
                answer = "EMPTY"
                if heap_max and heap_min:
                    answer = f"{-heap_max[0][0]} {heap_min[0][0]}"
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
            inputs.append(read_file(f"이중 우선순위 큐/input{i}.txt"))
            answers.append(read_file(f"이중 우선순위 큐/output{i}.txt"))
        self.assertEqual([main(inputs)], answers)


if __name__ == '__main__':
    unittest.main()