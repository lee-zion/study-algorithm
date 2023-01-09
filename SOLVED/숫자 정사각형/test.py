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
            xM, yM = map(int, input[0].split())
            rect = []
            answer = 0
            for i in range(xM):
                rect.append(input[1+i])
            for side in range(min(xM, yM) + 1):
                for x in range(xM - side):
                    for y in range(yM - side):
                        point = rect[x][y]
                        dx = [0, side, side]
                        dy = [side, 0, side]
                        for i in range(3):
                            nx = x + dx[i]
                            ny = y + dy[i]
                            if rect[x][y] == rect[nx][ny]:
                                continue
                            else:
                                point = -1
                                break
                        if point == -1:
                            continue
                        answer = max(answer, (side+1)**2)
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
            inputs.append(read_file(f"숫자 정사각형/input{i}.txt"))
            answers.append(int(read_file(f"숫자 정사각형/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()