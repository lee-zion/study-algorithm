import unittest
from traceback import print_exception
import sys, string

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
            """
            ord(a) = 97
            ord(z) = 122

            a, a -> z

            abcdefghijklmnopqrstuvwxyz
            abcdefghijklmnopqrstuvwxyz

            key = password[i % len(password)]
            offset = ord(c) - ord(key)
            c_encryped = c?ord(c)? - offset - 1
            answer += chr(c_encryped)

            mapping function
                    ord_min     ord_max
            char    a           z
            ord     97          122
            expect  0           25
            
            example)
            ord("c"), ord("v") = 99, 118
            offset = ord("v") - 96 (= 22)
            chr((ord("c") - ORD_OFFSET_FROM_ONE - OFFSET) % N_LOWERCASES + ORD_OFFSET_FROM_ONE)
            """
            plain, passphrase = input[0], input[1]
            WHITESPACE = 32
            ORD_OFFSET_FROM_ZERO = 96
            ORD_OFFSET_FROM_ONE = 97
            N_LOWERCASES = len(string.ascii_lowercase)
            answer = ""
            for i, c in enumerate(plain):
                if ord(c) == WHITESPACE:
                    answer += c
                else:
                    key = passphrase[i % len(passphrase)]
                    offset = ord(key) - ORD_OFFSET_FROM_ZERO
                    temp = chr((ord(c) - ORD_OFFSET_FROM_ONE - offset) % N_LOWERCASES + ORD_OFFSET_FROM_ONE)
                    answer += temp
            answers.append([answer])
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
            inputs.append(read_file(f"암호/input{i}.txt"))
            answers.append(read_file(f"암호/output{i}.txt"))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()