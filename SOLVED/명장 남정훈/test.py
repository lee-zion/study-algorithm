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

def main(inputs):
    answers = []
    try:
        for input in inputs:
            # your code here
            """
            - what if left > right?
            diff = left - right
              - what if all > diff:
              all -= diff
              right = left
              answer = left + right + all // 2 * 2
              
              - what if all < diff:
              right += all
              left = right
              answer = left + right
              
              - what if all == diff:
              right = left (all = 0)
              answer = left + right

            - what if right > left?
            same with the case above

            - what if left == right?
            answer = left + right + all // 2 * 2

            diff = left - right
            if diff > all:
                right += all
            else:
                # all >= diff
                right = left
                all -= diff
                answer = max(left, right) * 2
            """
            left, right, all = map(int, input[0].split())
            diff = abs(left - right)
            if diff == 0:
                answer = left + right + all // 2 * 2
            elif all > diff:
                answer = (max(left, right) + all // 2) * 2
            else:
                answer = (min(left, right) + all) * 2
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
        for i in range(1, 2 + 1):
            inputs.append(read_file(f"명장 남정훈/input{i}.txt"))
            answers.append(int(read_file(f"명장 남정훈/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()