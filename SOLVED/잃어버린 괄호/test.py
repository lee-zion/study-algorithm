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
    # 규칙
    # 시작끝 숫자
    # 연속 연산자 X
    # 5자리 이하의 숫자
    # 0으로 시작 가능
    # 총 길이 50 이하
    answers = []
    try:
        for input in inputs:
            eqn = input[0]
            eqn_minus = eqn.split("-")
            for i in range(len(eqn_minus)):
                # if begins with zero
                eqn_plus = eqn_minus[i].split("+")
                # expected state of eqn_plus[j]
                # 1, 11, ..., 11111, 01, 001, ..., 00001, ..., 01111, 0, 00, ..., 00000
                for j in range(len(eqn_plus)):
                    if eqn_plus[j][0] == "0":
                        # 01, 001, ..., 00001, ..., 01111, 0, 00, ..., 00000
                        ix = next((i for i, x in enumerate(eqn_plus[j]) if int(x)), None)
                        # eqn_plus[j] = eqn_plus[j][ix:] if ix else "0"
                        if ix:
                            # 01, 001, ..., 00001, ..., 01111
                            eqn_plus[j] = eqn_plus[j][ix:]
                        else:
                            # 0, 00, ..., 00000
                            eqn_plus[j] = "0"
                    # sum(eqn_plus[j])
                    # else:
                        # 1, 11, ..., 11111
                        # do nothing
                # [..., "40+50", ...] -> [..., "90", ...]
                eqn_minus[i] = str(sum(map(int, eqn_plus)))
                # eqn_minus = eqn_minus[:i] + eqn_plus + eqn_minus[(i+1):]
            # expected state of eqn_plus
            # ["46", "234", "3", "4646", "34674236", ...]
            answer = eval(eqn_minus[0])
            if len(eqn_minus) > 1:
                for eqn_part in eqn_minus[1:]:
                    answer -= eval(eqn_part)
            answers.append(str(answer))
        return answers
    except Exception as e:
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
            inputs.append(read_file(f"잃어버린 괄호/input{i}.txt"))
            answers.append(read_file(f"잃어버린 괄호/output{i}.txt")[0])
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()