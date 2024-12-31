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
            calculate prefix-sum to determine given section is all 0's or 1's

            def sum(x1, y1, x2, y2):
                nonlocal prefix_sum
                total_sum = prefix_sum[x2][y2]
                top_sum = 0 if x1 == 0 else prefix_sum[x1-1][y2]
                left_sum = 0 if y1 == 0 else prefix_sum[x2][y1-1]
                duplicated = prefix_sum[x1-1][y1-1] if x1 > 0 and y1 > 0 else 0
                return total_sum - top_sum - left_sum + duplicated
            """
            n = int(input[0])
            grid = []
            for i in range(n):
                grid.append(list(map(int, input[i+1].split())))
            
            prefix_sum = [[0]*n for _ in range(n)]
            
            for x in range(n):
                for y in range(n):
                    if x == 0 or y == 0:
                        if x == 0:
                            prefix_sum[x][y] = grid[x][y] + prefix_sum[x][y-1]
                        else:
                            prefix_sum[x][y] = grid[x][y] + prefix_sum[x-1][y]
                    else:
                        upper = prefix_sum[x-1][y]
                        left = prefix_sum[x][y-1]
                        prefix_sum[x][y] = grid[x][y] + upper + left - prefix_sum[x-1][y-1]
            
            def get_partial_sum(x1, y1, x2, y2):
                nonlocal prefix_sum
                total_sum = prefix_sum[x2][y2]
                top_sum = 0 if x1 == 0 else prefix_sum[x1-1][y2]
                left_sum = 0 if y1 == 0 else prefix_sum[x2][y1-1]
                duplicated = prefix_sum[x1-1][y1-1] if x1 > 0 and y1 > 0 else 0
                return total_sum - top_sum - left_sum + duplicated
            
            blue, white = 0, 0
            
            candidates = []
            candidates.append((0, 0, n-1, n-1, n))
            while candidates:
                x1, y1, x2, y2, paper = candidates.pop()
                print("current piece:")
                for x in range(x1, x2+1):
                    print(grid[x][y1:y2+1])
                partial_sum = get_partial_sum(x1, y1, x2, y2)
                if partial_sum == paper * paper:
                    print("Succeed!")
                    blue += 1
                elif partial_sum == 0:
                    print("Succeed!")
                    white += 1
                else:
                    print("Failed, split into pieces")
                    half_x, half_y = (x1 + x2) // 2, (y1 + y2) // 2
                    half_paper = paper // 2
                    candidates.append((x1, y1, half_x, half_y, half_paper))
                    candidates.append((half_x + 1, y1, x2, half_y, half_paper))
                    candidates.append((x1, half_y + 1, half_x, y2, half_paper))
                    candidates.append((half_x + 1, half_y + 1, x2, y2, half_paper))
            
            answers.append(str(white))
            answers.append(str(blue))
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
            inputs.append(read_file(f"색종이 만들기/input{i}.txt"))
            answers.append(read_file(f"색종이 만들기/output{i}.txt"))
        self.assertEqual(main(inputs), answers[0])


if __name__ == '__main__':
    unittest.main()