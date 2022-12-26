import unittest
from traceback import print_exception
import sys, string
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
            s, n = string.ascii_uppercase[:6], string.digits[1:7]
            cmd = []
            [cmd.append(input[i]) for i in range(36)]
            if len(list(set(cmd))) != len(cmd):
                answer = "Invalid"
                answers.append(answer)
                continue
            cmd.append(cmd[0])
            found = deque([(s.find(cmd[0][0]), n.find(cmd[0][1]))])
            is_valid = True
            for c in cmd[1:]:
                psi, pni = found.popleft()
                si, ni = s.find(c[0]), n.find(c[1])
                asi, ani = abs(si - psi), abs(ni - pni)
                if (asi == 2 and ani == 1) or (asi == 1 and ani == 2):
                    found.append((si, ni))
                else:
                    is_valid = False
                    break
            answer = "Valid" if is_valid else "Invalid"
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
            inputs.append(read_file(f"나이트 투어/input{i}.txt"))
            answers.append(read_file(f"나이트 투어/output{i}.txt")[0])
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()