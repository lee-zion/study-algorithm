import unittest
from traceback import print_exception
import sys

def read_file(filename):
    file = open(filename, 'r')
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret

class Node(object):
    def __init__(self, item) -> None:
        self.item = item
        self.left = self.right = None

class BinaryTree(object):
    def __init__(self) -> None:
        self.root = None

def main(inputs):
    answers = []
    try:
        for input in inputs:
            # your code here
            n = int(input[0])
            graph = []
            for i in range(n-1):
                parent, child, weight = list(map(int, input[1+i].split()))
                
            answer = True

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
            inputs.append(read_file(f"트리의 지름/input{i}.txt"))
            answers.append(int(read_file(f"트리의 지름/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()