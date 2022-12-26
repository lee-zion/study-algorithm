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
            offset = 0
            n_group, groups = 0, []
            def nasty(writer, receiver):
                return f"{writer} was nasty about {receiver}"
            def no_nasty():
                return "Nobody was nasty"
            while True:
                group = []
                n = int(input[offset])
                if n == 0:
                    break
                for i in range(n):
                    offset += 1
                    group.append(input[offset].split())
                offset += 1
                groups.append(group)
            
            for ig, group in enumerate(groups):
                if ig != 0:
                    answers.append("")
                answers.append(f"Group {ig+1}")
                for ip, paper in enumerate(group):
                    for i, comment in enumerate(paper[1:]):
                        if comment == "N":
                            answers.append(nasty(group[(ip-i-1) % len(group)][0], paper[0]))
                if answers[-1] == f"Group {ig+1}":
                    answers.append(no_nasty())
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
            inputs.append(read_file(f"메시지/input{i}.txt"))
            answers.append(read_file(f"메시지/output{i}.txt"))
        self.assertEqual(main(inputs), answers[0])


if __name__ == '__main__':
    unittest.main()