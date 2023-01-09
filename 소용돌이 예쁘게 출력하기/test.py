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
            x1, y1, x2, y2 = map(int, input[0].split())
            nx, ny = x2 - x1 + 1, y2 - y1 + 1
            paper = [[0] * ny for _ in range(nx)]
            xM = max(abs(x1), abs(x2))
            yM = max(abs(y1), abs(y2))
            M = max(xM, yM)
            n = M*2 + 1
            # paper = [[-1]*n for _ in range(n)] # 최대 10k x 10k = 100M
            offset = {
                'x': n // 2,
                'y': max(n // 2, 0)
            }
            left_top = 1 + n
            
            # paper[offset[x]][offset[y]] = 1

            def get_number(x, y):
                ret = 0
                # 1 + 2 + ... + x-1 = x(x-1) / 2
                x_step = abs(x)-1
                y_step = abs(y)-1
                # x_step = x-1 if x > 0 else -x-1
                # y_step = y-1 if y > 0 else -y-1
                # ret = 8 * (x_step + y_step)
                x0 = x - x_step if x > 0 else x + x_step
                y0 = y - y_step if y > 0 else y + y_step
                dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
                dy = [0, 1, 1, 0, -1, -1, -1, 0, 1]
                step = -1
                for i in range(9):
                    if x0 == dx[i] and y0 == dy[i]:
                        ret += i + 1
                        step = i
                        break
                for i in range(x_step + y_step):
                    ret += (step + i * 8)
                return ret
            temp = get_number(3, -3)
            print(temp)
            """
            230103
            |x|, |y| <= 0 ---> n <= (2*0 + 1)^2 = 1
            |x|, |y| <= 1 ---> n <= (2*1 + 1)^2 = 9
            |x|, |y| <= 2 ---> n <= (2*2 + 1)^2 = 25
            |x|, |y| <= 3 ---> n <= (2*3 + 1)^2 = 49

            spiral process
            given
            n = 2*max(abs(x), abs(y)) + 1
            n_max = n**2
            line = range(n) - 1

            n = max(abs(x), abs(y))
            spiral_max = n**2
            for line in [1, 3, 5, ... 2n+1]:
                line


            1. (nx, ny) = (x, y) + (0, 1)
            2. (nx, ny) = (x, y) + (-i, 0) for i in range(1, l)
            3. (nx, ny) = (x, y) + (0, -i) for i in range(1, l+1)
            4. (nx, ny) = (x, y) + (i, 0) for i in range(1, l+1)
            3. 


            ----------
            x1, y1에서 절대값이 작은 아이를 m이라고 하고, 큰 아이를 M이라고 하자
            이 때 paper[x1][y1] = paper[m][m] + M-m
            paper[m][m] = paper[x0][y0] + step(m)



                        x1  x2  y1  y2  Mx  My
            ni <= 1^2    0   0   0   0  0   0
            ni <= 2^2   -1   0   0   1  1   1
            ni <= 3^2   -1   1  -1   1  1   1
            ni <= 4^2   -2   1  -1   2  2   2
            ni <= 5^2   -2   2  -2   2  2   2
            ...
            ni in [max(x) * 2, max(x) * 2 + 1]



            find paper[x][y] pattern
            1 -> 2 -> 11 -> 28 -> ... ; +1 +9 +17 ... ; +8 +8 ...
            1 -> 3 -> 13 -> 31 -> ... ; +2 +10 +18 ...; +8 +8 ...
            ...
            1 -> 9 -> 25 -> 49 -> ... ; +8 +16 +24 ...; +8 +8 ...
            limitation; only diagonal elements are calculatable
            ->
            paper[1][2] = ?
            paper[1][1] = 9 -> move (0, 1) from x=1, y=1



            TODO:
            def get_paper(x, y, xM, yM, M):
                ret = 0
                while x > 0:
                    x -= 1
                    ret += 8
                while y > 0:
                    y -= 1
                    ret += 8
                (0, 0), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)
                -> 1, 2, 3, 4, 5, 6, 7, 8, 9
                return 

            find paper begin index

            n   M       p0
            1   0       0, 0
            2   0.5     1, 0
            3   1       1, 1
            4   1.5     2, 1
            5   2       2, 2
            ...
            x, y        n//2, (n-1)//2



            1   : -1, 0
            odd : -1,-1  (except 1)
            even:  1, 1
            n <= 1^2 ----> xi = [ 0, 0]
                           yi = [ 0, 0]
            n <= 2^2 ----> xi = [-1, 0]     + (-1, 0)
                           yi = [ 0, 0]     + ( 0, 0)
            n <= 3^2 ----> xi = [-1, 1]     + ( 0, 1)
                           yi = [-1, 1]     + (-1, 1)
            n <= 4^2 ----> xi = [-2, 1]     + (-1, 0)
                           yi = [-1, 2]     + ( 0, 1)
            n <= 5^2 ----> xi = [-2, 2]     + ( 0, 1)
                           yi = [-1, 2]     + (-1, 0)
            n <= 6^2 ----> xi = [-3, 2]     + (-1, 0)
                           yi = [-3, 2]     + (-1, 0)
            n <= 7^2 ----> xi = [-3, 3]     + ( 0, 1)
                           yi = [-3, 3]     + (-1, 0)

            max(x)  n
            0       1
            1       2, 3
            2       4, 5
            3       6, 7
            
            max(y)  n
            0       1, 2
            1       -
            2       4, 5, 6
            3       7, 8
            """
            # left, right = 
            answer = True
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
        for i in range(1, 4 + 1):
            inputs.append(read_file(f"소용돌이 예쁘게 출력하기/input{i}.txt"))
            answers.append(read_file(f"소용돌이 예쁘게 출력하기/output{i}.txt"))
        self.assertEqual(main(inputs), answers[0])


if __name__ == '__main__':
    unittest.main()