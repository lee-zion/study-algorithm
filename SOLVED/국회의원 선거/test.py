import unittest
from traceback import print_exception
import heapq
import sys

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
            N = a1 a2 ... an
            s = sum(N)
            """
            votes = []
            for i in range(int(input[0])):
                votes.append(int(input[1+i]))
            mine = votes[0]
            max_heap = []
            for vote in votes:
                heapq.heappush(max_heap, -vote)
            
            answer = 0
            while True:
                competitor = -heapq.heappop(max_heap)
                if mine > competitor:
                    break
                competitor -= 1
                heapq.heappush(max_heap, -competitor)
                mine += 1
                answer += 1
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
        for i in range(6, 6 + 1):
            inputs.append(read_file(f"국회의원 선거/input{i}.txt"))
            answers.append(int(read_file(f"국회의원 선거/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()