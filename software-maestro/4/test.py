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
            n = int(input[0])
            chopsticks = input[1].split()
            done = [[2, 0, 0, 0], [0, 2, 0, 0], [0, 0, 2, 0], [0, 0, 0, 2]]
            board = [[0] * 4 for _ in range(n)]
            for i, chop in enumerate(chopsticks):
                for c in chop:
                    if c == "A":
                        board[i][0] += 1
                    elif c == "B":
                        board[i][1] += 1
                    elif c == "C":
                        board[i][2] += 1
                    elif c == "D":
                        board[i][3] += 1
            def is_solved(board):
                """
                if there are no 1 in board, consider as solved
                """
                for row in board:
                    for i in range(4):
                        if row[i] == 1:
                            return False
                return True
            
            def get_common_idx(board, i, j):
                cid = -1
                for col in range(4):
                    if board[i][col] == 1 and board[j][col] == 1:
                        cid = col
                        # even if common has 2 elements, it is okay to ignore it.
                        break
                return cid
            
            answer = 0
            while True:
                if is_solved(board):
                    break
                
                for i in range(n):
                    curr = board[i]
                    if curr in done:
                        continue
                    
                    for j in range(n):
                        if i == j:
                            continue
                        
                        new = board[j]
                        common = get_common_idx(board, i, j)
                        if common == -1:
                            continue
                        
                        for col in range(4):
                            if col == common:
                                curr[common] += 1
                                new[common] -= 1
                            elif curr[col] == 1:
                                curr[col] -= 1
                                new[col] += 1
                        diff = abs(i - j)
                        answer += diff * 2 - 1 if diff != 1 else 1
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
            inputs.append(read_file(f"software-maestro/4/input{i}.txt"))
            answers.append(int(read_file(f"software-maestro/4/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()