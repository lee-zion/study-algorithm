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
            # Category: Serialize/Deserialize of Binary Tree
            # https://bellog.tistory.com/146
            # 
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
            # ex) a+b+c+d = abc
            #        _____+_____
            #       /           \
            #      a           __+__
            #                 /     \
            #                b     __+__
            #                     /     \ 
            #                    c       d
            # -->
            #        _____+_____
            #       /           \
            #      a           bcd++
            # -->
            #           abcd+++
            # 
            given: str = input[0]
            # operators = ["(", ")"]
            operators = ["+", "-", "*", "/", "(", ")"]

            seq = []
            for i in given:
                if i in operators:
                    seq.append(i)
                else:
                    seq.append(i)
            print(seq)

            def deserialize(str):
                
            # operators = [
            #     "([(|)])",
            #     "([*|/])",
            #     "([+|-])",
            # ]
            # for operator_group in operators:
            #     given = re.split(operator_group, given)
            #     # for part in given:
            #     #     if part in operators[1:-1].split("|"):
                        
            #     # given.find
            #     # How to find string
            #     # 1. inside parenthesis ()
            #     # 2. near * / + -
            #     # given = re.split(operator_group, given)
            #     # given = list(filter(None, re.split(operator_group, given)))
            #     for i in range(len(given)):
            #         print(given[i])
            #         # (, ), *, /, +, -
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