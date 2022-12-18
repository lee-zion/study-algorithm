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
    def flip(l, pos):
        l[pos] = "1" if l[pos] == "0" else "0"
    try:
        for input in inputs:
            # your code here
            MALE = 1
            n_switch = int(input[0])
            switch = [""] + input[1].split()
            n_student = int(input[2])
            for student in range(n_student):
                sex, given = map(int, input[3 + student].split())
                if sex == MALE:
                    # MALE
                    i = 1
                    while True:
                        # switch[given * i] = bin(~f"0b{switch[given * i]}")
                        flip(switch, given * i)
                        i += 1
                        if given * i > n_switch:
                            break
                else:
                    # FEMALE
                    flip(switch, given)
                    offset = 1
                    while True:
                        if given + offset > n_switch or given - offset <= 0:
                            break
                        if switch[given + offset] == switch[given - offset]:
                            flip(switch, given + offset)
                            flip(switch, given - offset)
                            offset += 1
                        else:
                            break
            answer = []
            switch = switch[1:]
            for i in range(1 + n_switch // 20):
                answer.append(' '.join(switch[20*i:20*(i+1)]))
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
        for i in range(1, 3 + 1):
            inputs.append(read_file(f"스위치 켜고 끄기/input{i}.txt"))
            answers.append(read_file(f"스위치 켜고 끄기/output{i}.txt"))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()