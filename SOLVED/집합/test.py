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
            answer = []
            s = set()
            n = int(input[0])
            for i in range(1, n+1):
                cmd = input[i]
                if cmd == "all":
                    s = set(str(i) for i in range(1, 21))
                elif cmd == "empty":
                    s.clear()
                else:
                    cmd, x = cmd.split()
                    # x = int(x)
                    if cmd == "add":
                        s.add(x)
                    elif cmd == "remove":
                        s.discard(x)
                    elif cmd == "check":
                        if x in s:
                            answer.append("1")
                        else:
                            answer.append("0")
                    elif cmd == "toggle":
                        if x in s:
                            s.discard(x)
                        else:
                            s.add(x)
                    else:
                        print(f"Unknown command {cmd}")
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
        for i in range(1, 1 + 1):
            inputs.append(read_file(f"집합/input{i}.txt"))
            answers.append(read_file(f"집합/output{i}.txt"))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()