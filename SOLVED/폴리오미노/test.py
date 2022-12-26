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
            board = input[0].split(".")
            is_solvable = True
            for i, piece in enumerate(board):
                if piece:
                    l = len(piece)
                    if l % 2 == 0:
                        # piece is solvable
                        replacer = ""
                        while True:
                            if l >= 4:
                                l -= 4
                                replacer += "A"*4
                            elif l >= 2:
                                l -= 2
                                replacer += "B"*2
                            else:
                                break
                        board[i] = replacer
                    else:
                        is_solvable = False
                        break
            # board = " ".join(input[0].split("."))
            answer = ".".join(board) if is_solvable else "-1"
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
            inputs.append(read_file(f"폴리오미노/input{i}.txt"))
            answers.append(read_file(f"폴리오미노/output{i}.txt")[0])
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()