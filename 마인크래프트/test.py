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
            TIME_INIT, BLOCK_INIT = -1, 257
            X_MAX, Y_MAX, block = map(int, input[0].split())
            lands = []
            h_min, h_max = 0, 0
            for i in range(X_MAX):
                land = list(map(int, input[1+i].split()))
                h_min, h_max = min(h_min, min(land)), max(h_max, max(land))
                lands.append(land)
            
            diff = [[0] * Y_MAX for _ in range(X_MAX)]
            ddic = {}
            # diff is land - h_min
            # if   diff[x][y] > 0: cost += diff[x][y] * 2 (블록 제거)
            # elif diff[x][y] < 0: cost += diff[x][y], block -= 1 (블록 놓음)
            # else (diff[x][y] == 0; 목표 높이와 같은 상태)
            for x in range(X_MAX):
                for y in range(Y_MAX):
                    subtract = lands[x][y] - h_min
                    ddic[subtract] = ddic[subtract] + 1 if subtract in ddic else 1
                    diff[x][y] = subtract
            
            answer = (TIME_INIT, BLOCK_INIT)
            for target in range(0, h_max - h_min + 1):
                cost, block_needed = 0, 0
                for key in ddic.keys():
                    subtract = key - target
                    if subtract > 0:
                        cost += ddic[key] * 2 * subtract
                    elif subtract < 0:
                        cost += ddic[key]
                        block_needed += ddic[key]
                if block < block_needed:
                    break
                if answer[0] != TIME_INIT:
                    if cost <= answer[0]:
                        answer = (cost, h_min + target)
                else:
                    answer = (cost, h_min + target)
            answers.append([f"{answer[0]} {answer[1]}"])
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
        for i in range(9, 15 + 1):
            inputs.append(read_file(f"마인크래프트/input{i}.txt"))
            answers.append(read_file(f"마인크래프트/output{i}.txt"))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()