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
            """
            prefix_sum of 2D array

            a[x1][y1] + ... + a[x2][y1]
            + ...
            + a[x1][y2] + ... + a[x2][y2]
            =
            sum[x2][y2] - a[x1-1][y2] - a[x2][y1-1] + a[x1-1][y1-1]
            """
            n_grid, n_problem = map(int, input[0].split())
            grid = []
            prefix_sum = [[0] * n_grid for _ in range(n_grid)]
            answer = []
            for i in range(n_grid):
                grid.append(list(map(int, input[1+i].split())))

            for x in range(n_grid):
                for y in range(n_grid):
                    top = 0 if x == 0 else prefix_sum[x-1][y]
                    left = 0 if y == 0 else prefix_sum[x][y-1]
                    diag = 0 if x == 0 or y == 0 else prefix_sum[x-1][y-1]
                    prefix_sum[x][y] = grid[x][y] + left + top - diag
            
            for i in range(n_problem):
                x1, y1, x2, y2 = map(int, input[1 + n_grid + i].split())
                # x1, y1 = x1 - 1, y1 - 1
                x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
                diag = 0 if x1 == 0 or y1 == 0 else prefix_sum[x1-1][y1-1]
                left = 0 if y1 == 0 else prefix_sum[x2][y1-1]
                top = 0 if x1 == 0 else prefix_sum[x1-1][y2]
                answer.append(str(prefix_sum[x2][y2] + diag - top - left))
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
        for i in range(1, 2 + 1):
            inputs.append(read_file(f"구간 합 구하기 5/input{i}.txt"))
            answers.append(read_file(f"구간 합 구하기 5/output{i}.txt"))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()