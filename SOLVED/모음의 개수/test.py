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
            vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
            offset = 0
            while True:
                sentence: str = input[offset]
                if sentence == "#":
                    break
                n_vowel = 0
                for s in sentence:
                    if s in vowels:
                        n_vowel += 1
                answers.append(n_vowel)
                offset += 1
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
            inputs.append(read_file(f"모음의 개수/input{i}.txt"))
            answers.append(list(map(int, read_file(f"모음의 개수/output{i}.txt"))))
        self.assertEqual(main(inputs), answers[0])


if __name__ == '__main__':
    unittest.main()