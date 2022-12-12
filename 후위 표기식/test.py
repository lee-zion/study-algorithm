import unittest
from traceback import print_exception
import sys
import re

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
            # idea
            # tree 구조로 치환한 뒤 leaf부터 root까지, 왼쪽에서 오른쪽으로 이동
            # 
            # ex) a*(b+c) = abc+*
            #        _____*_____
            #       /           \
            #      a           __+__
            #                 /     \
            #                b       c
            # -->
            #        _____*_____
            #       /           \
            #      a            bc+
            # -->
            #           abc+*
            # 
            # ex) a*b+c = ab*c+
            #        _____+_____
            #       /           \
            #    __*__           c
            #   /     \
            #  a       b
            # -->
            #        _____+_____
            #       /           \
            #     ab*            c
            # -->
            #           ab*c+
            # 
            # ex) a+b*c = abc*+
            #        _____+_____
            #       /           \
            #      a           __*__
            #                 /     \
            #                b       c
            # -->
            #        _____+_____
            #       /           \
            #      a            bc*
            # -->
            #           abc*+
            # 
            class BinaryTree:
                def __init__(self) -> None:
                    self.root = None
                def postorder(self):
                    order = ""
                    def _postorder(node: Node):
                        nonlocal order
                        if node.left:
                            _postorder(node.left)
                        if node.right:
                            _postorder(node.right)
                        order += node.item
                    return order
            class Node:
                def __init__(self, item) -> None:
                    self.item = item
                    self.left = self.right = None
            
            tree = BinaryTree()
            
            given: str = input[0]
            operators = [
                "([(|)])",
                "([*|/])",
                "([+|-])",
            ]
            for operator_group in operators:
                given = re.split(operator_group, given)
                # for part in given:
                #     if part in operators[1:-1].split("|"):
                        
                # given.find
                # How to find string
                # 1. inside parenthesis ()
                # 2. near * / + -
                # given = re.split(operator_group, given)
                # given = list(filter(None, re.split(operator_group, given)))
                for i in range(len(given)):
                    print(given[i])
                    # (, ), *, /, +, -
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
        for i in range(1, 4 + 1):
            inputs.append(read_file(f"후위 표기식/input{i}.txt"))
            answers.append(read_file(f"후위 표기식/output{i}.txt")[0])
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()