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
            POSSIBLE_MAX = 64
            row, col = map(int, input[0].split())
            board = []
            for i in range(row):
                temp = []
                # white == True, black == False
                for j in input[1+i]:
                    temp.append(False) if j == "B" else temp.append(True)
                board.append(temp)
            repair_tbl = [[POSSIBLE_MAX] * (col - 7) for _ in range(row - 7) ]
            
            for x in range(row - 7):
                for y in range(col - 7):
                    repair_by_case = [0, 0]
                    for case in range(2):
                        for dx in range(8):
                            for dy in range(8):
                                nx, ny = x + dx, y + dy
                                # case 0: expect wb.. == True False .. --> if x+y is odd, expect False
                                # case 1: expect bw.. == False True .. --> if x+y is odd, expect True
                                
                                if (nx + ny)%2 == case:
                                    # case 0: is even(0,2,4,6) == expect True
                                    # case 1: is odd(1,3,5,7) == expect True
                                    if not board[nx][ny]:
                                        repair_by_case[case] += 1
                                else:
                                    # case 0: is odd == expect False
                                    # case 1: is even == expect False
                                    if board[nx][ny]:
                                        repair_by_case[case] += 1
                    repair_tbl[x][y] = min(repair_tbl[x][y], min(repair_by_case))
            answer = min([min(r) for r in repair_tbl])
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
        for i in range(1, 7 + 1):
            inputs.append(read_file(f"체스판 다시 칠하기/input{i}.txt"))
            answers.append(read_file(f"체스판 다시 칠하기/output{i}.txt")[0])
        self.assertEqual(main(inputs), list(map(int, answers)))


if __name__ == '__main__':
    unittest.main()