import unittest
from traceback import print_exception
import sys
from collections import deque

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
            answer = deque([])
            n = int(input[0])
            # 숫자 x가 주어졌을 때, 이후의 x보다 작은 숫자들의 순서가 
            curr = 1
            stack = deque([])
            for i in range(n):
                dest = int(input[1+i])
                while dest >= curr:
                    stack.append(curr)
                    answer.append("+")
                    curr += 1
                top = stack.pop() if stack else None
                if top == dest:
                   answer.append("-") 
                else:
                    answer = deque(["NO"])
                    break
            # [answers.append(answer.popleft()) for _ in range(len(answer))]
            answers.append(list(answer))
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
            inputs.append(read_file(f"스택 수열/input{i}.txt"))
            answers.append(read_file(f"스택 수열/output{i}.txt"))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()