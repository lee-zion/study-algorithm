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
            1 -> 1
            2 -> 0
            3 -> 0
            4 -> 2 / (2, 4, 1, 3), (3, 1, 4, 2)
            5 -> 
            """
            n = int(input[0])
            grid = [[0] * n for _ in range(n)]
            answer = 0

            def is_attackable_from(x, y, grid):
                """
                Check row/column/diag+/diag-
                """
                row = sum([grid[x][i] for i in range(n)])
                if row != 1:
                    return True
                
                col = sum([grid[i][y] for i in range(n)])
                if col != 1:
                    return True
                
                diag1, diag2 = 1, 1
                for i in range(1, n):
                    x_upper, x_lower = x-i, x+i
                    y_left, y_right = y-i, y+i
                    if x_lower < n and y_right < n:
                        diag1 += grid[x_lower][y_right]
                    if x_lower < n and y_left >= 0:
                        diag1 += grid[x_lower][y_left]
                    if x_upper >= 0 and y_right < n:
                        diag2 += grid[x_upper][y_right]
                    if x_upper >= 0 and y_left >= 0:
                        diag2 += grid[x_upper][y_left]
                if diag1 != 1 or diag2 != 1:
                    return True
                return False

            def dfs(col, grid, visited):
                nonlocal answer
                for i in range(n):
                    if i in visited:
                        continue
                    grid[i][col] = 1
                    visited.add(i)
                    if not is_attackable_from(i, col, grid):
                        if col == n-1:
                            answer += 1
                        else:
                            dfs(col+1, grid, visited)
                    grid[i][col] = 0
                    visited.remove(i)
            
            visited = set()
            dfs(0, grid, visited)
            # for i in range(n):
            #     dfs(i, grid, visited)
            answers.append([str(answer)])
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
        for i in range(1, 6 + 1):
            inputs.append(read_file(f"N-Queen/input{i}.txt"))
            answers.append(read_file(f"N-Queen/output{i}.txt"))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()