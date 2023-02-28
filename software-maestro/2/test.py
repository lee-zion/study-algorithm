import unittest
from traceback import print_exception
import sys
from collections import deque

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
            n = int(input[0].strip())
            lines = []
            for _ in range(n):
                lines.append(list(map(int, input[1+_].strip().split())))
            MAX = 101
            grid = [[0] * MAX for _ in range(MAX)]
            for line in lines:
                x1, y1, x2, y2 = line
                for x in range(x1, x2+1):
                    for y in range(y1, y2+1):
                        grid[x][y] += 1
            crossed = deque()
            dx = [1, 0, -1, 0]
            dy = [0, 1, 0, -1]

            """
            TODO: Problem
            
            l1: (0, 3) -> (3, 3)
            l2: (3, 3) -> (6, 3)
            l3: (0, 3) -> (6, 3)
            l4: (3, 0) -> (3, 6)
            
            l3 and l4
            [0, 0, 0, 1, 0, 0, 0]
            [0, 0, 0, 1, 0, 0, 0]
            [0, 0, 0, 1, 0, 0, 0]
            [1, 1, 1, 2, 1, 1, 1]
            [0, 0, 0, 1, 0, 0, 0]
            [0, 0, 0, 1, 0, 0, 0]
            [0, 0, 0, 1, 0, 0, 0]
            
            l1+l2 and l4
            [0, 0, 0, 1, 0, 0, 0]
            [0, 0, 0, 1, 0, 0, 0]
            [0, 0, 0, 1, 0, 0, 0]
            [1, 1, 1, 3, 1, 1, 1]
            [0, 0, 0, 1, 0, 0, 0]
            [0, 0, 0, 1, 0, 0, 0]
            [0, 0, 0, 1, 0, 0, 0]

            
            ADVANCED PROBLEM
            l5:  (3, 0) -> (3, 1)
            l6:  (3, 1) -> (3, 2)
            l7:  (3, 2) -> (3, 3)
            l8:  (3, 3) -> (3, 4)
            l9:  (3, 4) -> (3, 5)
            l10: (3, 5) -> (3, 6)
            
            l1+l2 and sum(l5~l10)
            [0, 0, 0, 1, 0, 0, 0]
            [0, 0, 0, 2, 0, 0, 0]
            [0, 0, 0, 2, 0, 0, 0]
            [1, 1, 1, 4, 1, 1, 1]
            [0, 0, 0, 2, 0, 0, 0]
            [0, 0, 0, 2, 0, 0, 0]
            [0, 0, 0, 1, 0, 0, 0]
            
            What is definition of crossed point?
            -> Check the two statements below:
            1) Have up/down/left/right(UDLR) component
            2) value of the components are non-zero (positive)

            How to check size of cross from crossed point?
            -> From crossed point, iterate the following process:
            1) check the two statements for UDLR
            2) for each checked element
            2-1) for UD case, make sure that grid[nx][ny] has no horizontal line crossing
            -> if grid[nx][ny] == 1, it is obvious that no other line cross this point.
            but what if grid[nx][ny] > 1?
            --> FROM COUNTER #1-1, IT IS LIKELY TO OCCUR WITH SEGMENTED LINES. But 
            It is REALLY hard to distinguish it from CROSSING LINE, when lines exist NEAR THAT SEGMENTED.
            
            2-2) for LR case,

            COUNTER #1)
            how to DISTINGUISH 1-1 and 1-2?
            from our definiton of crossed point, 1-1 will have 2 crossed point, even if one is not actual crossing point
            as-is) crossed_point = [(3, 3), (4, 3)]
            to-be) crossed_point = [(3, 3)]
            TODO: ADVANCE on crossed point definition

            COUNTER #1-1) 
            l1: (0, 3) -> (6, 3)
            l2: (3, 0) -> (3, 3)
            l3: (3, 3) -> (3, 6)
            l4: (2, 4) -> (2, 6)
            l5: (4, 4) -> (4, 6)

            [0, 0, 1, 1, 1, 0, 0]
            [0, 0, 1, 1, 1, 0, 0]
            [0, 0, 1, 2, 1, 0, 0]
            [1, 1, 1, 3, 1, 1, 1]
            [0, 0, 0, 1, 0, 0, 0]
            [0, 0, 0, 1, 0, 0, 0]
            [0, 0, 0, 1, 0, 0, 0]
            --->
            AS-IS 3
            TO-BE 3


            COUNTER #1-2)
            l1: (0, 3) -> (6, 3)
            l2: (3, 0) -> (3, 6)
            l3: (2, 4) -> (4, 4)
            l4: (2, 5) -> (2, 6)
            l5: (4, 5) -> (4, 6)

            [0, 0, 1, 1, 1, 0, 0]
            [0, 0, 1, 1, 1, 0, 0]
            [0, 0, 1, 2, 1, 0, 0]
            [1, 1, 1, 2, 1, 1, 1]
            [0, 0, 0, 1, 0, 0, 0]
            [0, 0, 0, 1, 0, 0, 0]
            [0, 0, 0, 1, 0, 0, 0]
            ---> 
            AS-IS 3
            TO-BE 1

            (IN PROGRESS) COUNTER #2)
            
            PERFECT-INDISTINGUISHABLE COUNTER EXAMPLE!
            !!!!!!YOU SHOULD RE-DEFINE THE GRAPH!!!!!!

            COUNTER #2-1) 
            l1: (0, 3) -> (6, 3)
            l2: (3, 0) -> (3, 3)
            l3: (3, 3) -> (3, 5)
            l3: (3, 5) -> (3, 7)
            l4: (2, 5) -> (2, 7)
            l5: (4, 5) -> (4, 7)

            [0, 0, 1, 1, 1, 0, 0]
            [0, 0, 1, 1, 1, 0, 0]
            [0, 0, 1, 2, 1, 0, 0]
            [0, 0, 0, 1, 0, 0, 0]
            [1, 1, 1, 3, 1, 1, 1]
            [0, 0, 0, 1, 0, 0, 0]
            [0, 0, 0, 1, 0, 0, 0]
            [0, 0, 0, 1, 0, 0, 0]
            ---> 
            AS-IS 3
            TO-BE 3

            COUNTER #2-2) 
            l1: (0, 3) -> (6, 3)
            l2: (3, 0) -> (3, 3)
            l3: (3, 3) -> (3, 7)
            l3: (2, 5) -> (4, 5)
            l4: (2, 6) -> (2, 7)
            l5: (4, 6) -> (4, 7)

            [0, 0, 1, 1, 1, 0, 0]
            [0, 0, 1, 1, 1, 0, 0]
            [0, 0, 1, 2, 1, 0, 0]
            [0, 0, 0, 1, 0, 0, 0]
            [1, 1, 1, 3, 1, 1, 1]
            [0, 0, 0, 1, 0, 0, 0]
            [0, 0, 0, 1, 0, 0, 0]
            [0, 0, 0, 1, 0, 0, 0]
            --->
            AS-IS 3
            TO-BE 1


            SUMMARY)
            COUNTER 1에서는, CROSSING 처리만 값을 참고해서 어떻게 잘 하면 다 할 수 있을 것 같았다.
            그런데 COUNTER 2를 보면 서로 다른 line configuration이지만 같은 graph를 갖는다.
            결국 애초에 그래프 생성 방법부터 틀렸다.

            case를 나눠서 segmented line을 허용하지 않는 경우와 허용하는 경우를 나눠서 구현
            """
            for x in range(MAX):
                for y in range(MAX):
                    if grid[x][y] > 1:
                        is_valid = True
                        for i in range(4):
                            nx, ny = x + dx[i], y + dy[i]
                            if nx < 0 or ny < 0 or nx >= MAX or ny >= MAX:
                                is_valid = False
                                break
                            if grid[nx][ny] == 0:
                                is_valid = False
                                break
                        if is_valid:
                            crossed.append((x, y))

            answer = 0 if crossed else -1

            def check_adjacent_of(x, y, d, dir: str = "xy"):
                dx, dy = [d, 0, -d, 0], [0, d, 0, -d]
                if dir == "x":
                    dx = [d, -d]
                    dy = [0, 0]
                elif dir == "y":
                    dx = [0, 0]
                    dy = [d, -d]
                l = len(dx)
                for i in range(l):
                    nx, ny = x + dx[i], y + dy[i]
                    if nx < 0 or ny < 0 or nx >= MAX or ny >= MAX:
                        return False
                    if grid[nx][ny] == 0:
                        return False
            
            for cross in crossed:
                d = 1
                x, y = cross
                while True:
                    is_valid = True
                    if not check_adjacent_of(x, y, d, "xy"):
                        break
                    d += 1

                    dx = [d, 0, -d, 0]
                    dy = [0, d, 0, -d]
                    for i in range(4):
                        nx, ny = x + dx[i], y + dy[i]
                        is_pureline = True
                        if dx[i]:
                            ddx = [0, 0]
                            ddy = [1, -1]
                        else:
                            ddx = [1, -1]
                            ddy = [0, 0]

                        for i in range(2):
                            nnx, nny = nx + ddx[i], ny + ddy[i]
                            if nny < 0 or nny >= MAX:
                                continue
                            if grid[nnx][nny] > 1:
                                is_pureline = False
                                break
                        if not is_pureline:
                            is_valid = False
                            break
                        if nx < 0 or ny < 0 or nx >= MAX or ny >= MAX:
                            is_valid = False
                            break
                        if grid[nx][ny] == 0:
                            is_valid = False
                            break
                    if not is_valid:
                        break
                    d += 1
                answer = max(answer, d-1)
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
            inputs.append(read_file(f"software-maestro/2/input{i}.txt"))
            answers.append(int(read_file(f"software-maestro/2/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()