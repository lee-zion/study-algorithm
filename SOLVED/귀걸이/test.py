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
            offset, gi = 0, 1
            while True:
                name, logs = [-1], dict()
                n = int(input[offset])
                if n == 0:
                    break
                for i in range(n):
                    offset += 1
                    name.append(input[offset])
                for i in range(2*n - 1):
                    offset += 1
                    id = input[offset].split()[0]
                    logs[id] = logs[id] + 1 if id in logs else 1
                
                for key in logs.keys():
                    if logs[key] == 1:
                        answers.append(f"{gi} {name[int(key)]}")
                offset += 1
                gi += 1
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
            inputs.append(read_file(f"귀걸이/input{i}.txt"))
            answers.append(read_file(f"귀걸이/output{i}.txt"))
        self.assertEqual(main(inputs), answers[0])


if __name__ == '__main__':
    unittest.main()