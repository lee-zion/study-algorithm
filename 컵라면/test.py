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
            """
            현재 시간 t1에서 deadline이 t1인 task 대신 t2인 task를 고를 경우?

            """
            # your code here
            n = int(input[0])
            heap = []
            for i in range(n):
                dl_curr, reward = map(int, input[1+i].split())
                heapq.heappush(heap, (dl_curr, -reward))
            
            reward_acc = 0
            TOP, TIME, REWARD = 0, 0, 1
            while heap:
                dl_curr, reward_curr = heapq.heappop(heap)
                reward_acc -= reward_curr
                while heap and heap[TOP][TIME] == dl_curr:
                    heapq.heappop(heap)

            answers.append(reward_acc)
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
        for i in range(2, 2 + 1):
            inputs.append(read_file(f"컵라면/input{i}.txt"))
            answers.append(int(read_file(f"컵라면/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()