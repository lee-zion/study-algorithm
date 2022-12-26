import unittest
from traceback import print_exception
import sys
from collections import defaultdict

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
            answer = 0
            for i in range(int(input[0])):
                basket = defaultdict(list)
                has_passed = True
                for si, s in enumerate(input[1+i]):
                    if s in basket:
                        if si in basket[s]:
                            # MISSED
                            basket[s].append(si + 1)
                            continue
                        has_passed = False
                        break
                    else:
                        basket[s].append(si + 1)
                if has_passed:
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
        for i in range(1, 5 + 1):
            inputs.append(read_file(f"그룹 단어 체커/input{i}.txt"))
            answers.append(int(read_file(f"그룹 단어 체커/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()