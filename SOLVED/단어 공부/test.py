import unittest
from traceback import print_exception
import sys
from collections import Counter

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
            counter = Counter()
            for s in input[0].upper():
                counter[s] += 1
            item_max = counter.most_common(1)[0]
            len_max = len(list(filter(lambda x: x[1] == item_max[1], list(counter.items()))))
            answer = item_max[0] if len_max == 1 else "?"
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
        for i in range(1, 4 + 1):
            inputs.append(read_file(f"단어 공부/input{i}.txt"))
            answers.append(read_file(f"단어 공부/output{i}.txt")[0])
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()