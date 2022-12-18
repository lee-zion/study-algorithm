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
            n_pots, n_friend = map(int, input[0].split())
            pots = []
            for pot in range(n_pots):
                pots.append(int(input[1+pot]))
            bracket = [0, max(pots)]
            while bracket[1] - bracket[0] > 1e-06:
                mid = sum(bracket) / 2
                filled = 0
                for pot in pots:
                    filled += pot // mid
                if filled < n_friend:
                    bracket[1] = mid
                elif filled > n_friend:
                    bracket[0] = mid
                else:
                    # if filled == n_friend
                    # it is fine, but we need to find is it 
                    bracket[0] = mid
                # mid = mid - 1 if filled < n_friend else mid + 1

            answer = sum(bracket) // 2
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
            inputs.append(read_file(f"이상한 술집/input{i}.txt"))
            answers.append(int(read_file(f"이상한 술집/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()