import unittest
from traceback import print_exception
import sys, string
import re
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
            # given: str = input[0]
            # operators = ["(", ")"]
            # operators = ["+", "-", "*", "/", "(", ")"]
            # offset = 0
            # q = deque([])
            # def serialize(given, pattern: str):
            #     given = re.split(pattern, "".join(given))
            #     lg = len(given)
            #     for i in range(lg, -1, -1):
            #         if i+1 >= lg:
            #             continue
            #         if given[i+1] == "":
            #             q.append(given[i])
            #             given = given[:i] + given[i+1:]
            
            # serialize(given, '[()]')
            # given.split()
            # serialize(given, '[*/]')
            # serialize(given, '[+-]')
            # for i, s in enumerate(given):
            #     # if i + 1 + offset >= lg:
            #     #     continue
            #     if i + 1 >= lg:
            #         continue
            #     if given[i+1] == "":
            #         # offset += 1
            #         q.append(given[i])
            #         given = given[:i+1].append(given[i+2:]) if i + 2 < lg else given[:i+1]
            # def deserialize(str):

            # stack-based solution (common one)
            answer = ""
            operators = deque([])
            given: str = input[0]
            for s in given:
                if s in string.ascii_uppercase:
                    print(s)
                    answer += s
                else:
                    if s == "(":
                        operators.append(s)
                    elif s == ")":
                        while operators and operators[-1] != "(":
                            top = operators.pop()
                            print(top)
                            answer += top
                        operators.pop()
                    elif s in ["*", "/"]:
                        while operators and operators[-1] in ["*", "/"]:
                            top = operators.pop()
                            print(top)
                            answer += top
                        operators.append(s)
                    elif s in ["+", "-"]:
                        while operators and operators[-1] != "(":
                            top = operators.pop()
                            print(top)
                            answer += top
                        operators.append(s)
            while operators:
                top = operators.pop()
                print(top)
                answer += top

            print(answer)
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