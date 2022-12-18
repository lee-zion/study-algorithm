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
            DP 점화식
            graph[x][y] = graph[x][y] + max(graph[x-1][y], graph[x][y-1])
            """
            X_MAX, Y_MAX = map(int, input[0].split())
            land = [list(map(int, input[1+i].split())) for i in range(X_MAX)]
            # acc = [[0]*Y_MAX for _ in range(X_MAX)]
            
            for x in range(X_MAX):
                for y in range(Y_MAX):
                    left = land[x][y-1] if y > 0 else 0
                    upper = land[x-1][y] if x > 0 else 0
                    land[x][y] = land[x][y] + max(left, upper)
            # for i in range(m - 1, M):
            #     left = land[m-1][i-1] if m == X_MAX else land[i][m-2]
            #     upper = land[i-1][m-1] if m == X_MAX else land[m-2][i]
            #     if m == X_MAX:
            #         land[m-1][i] = max(left, upper)
            #     else:
            #         land[i][m-1] = max(left, upper)
            answer = land[X_MAX-1][Y_MAX-1]
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
            inputs.append(read_file(f"자원 캐기/input{i}.txt"))
            answers.append(int(read_file(f"자원 캐기/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()