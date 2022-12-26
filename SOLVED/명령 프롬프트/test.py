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
            files = []
            for i in range(int(input[0])):
                files.append(input[1+i])
            answer = ""
            for i in range(len(files[0])):
                is_all_same = True
                reference = files[0][i]
                for file in files[1:]:
                    if reference != file[i]:
                        is_all_same = False
                        break
                if is_all_same:
                    answer += reference
                else:
                    answer += "?"
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
            inputs.append(read_file(f"명령 프롬프트/input{i}.txt"))
            answers.append(read_file(f"명령 프롬프트/output{i}.txt")[0])
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()