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
            n, m = map(int, input[0].split())
            nums = deque([i for i in range(1, n+1)])
            targets = list(map(int, input[1].split()))

            def get_dist(target: int, _list: list):
                forward = _list.index(target)
                backward = len(_list) - forward
                distance = min(forward, backward)
                direction = 1 if distance == forward else -1
                return (distance, direction)
            answer = 0
            for target in targets:
                dist, dir = get_dist(target, nums)
                for _ in range(dist):
                    nums.append(nums.popleft()) if dir == 1 else nums.appendleft(nums.pop())
                    answer += 1
                nums.popleft()
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
        for i in range(1, 4 + 1):
            inputs.append(read_file(f"회전하는 큐/input{i}.txt"))
            answers.append(int(read_file(f"회전하는 큐/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()