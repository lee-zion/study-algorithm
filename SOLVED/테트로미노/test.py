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
            ROW_MAX, COL_MAX = map(int, input[0].split())
            graph = [list(map(int, input[1+i].split())) for i in range(ROW_MAX)]
            warrier = [
                [
                    [0, 0, 1, 1], # dx
                    [0, 1, 0, 1], # dy
                ]
            ]
            archer = [
                [
                    [0, 0, 0, 0],
                    [0, 1, 2, 3]
                ],
                [
                    [0, 1, 2, 3],
                    [0, 0, 0, 0]
                ],
            ]
            magician = [
                [
                    [0, 1, 2, 1],
                    [0, 0, 0, 1]
                ],
                [
                    [1, 0, 1, 2],
                    [0, 1, 1, 1]
                ],
                [
                    [0, 0, 1, 0],
                    [0, 1, 1, 2]
                ],
                [
                    [1, 0, 1, 1],
                    [0, 1, 1, 2]
                ],
            ]
            thief = [
                [
                    [0, 1, 2, 0],
                    [0, 0, 0, 1]
                ],
                [
                    [0, 1, 2, 2],
                    [0, 0, 0, 1]
                ],
                [
                    [0, 0, 1, 2],
                    [0, 1, 1, 1]
                ],
                [
                    [0, 1, 2, 2],
                    [1, 1, 1, 0]
                ],
                [
                    [0, 0, 0, 1],
                    [0, 1, 2, 2]
                ],
                [
                    [0, 0, 0, 1],
                    [0, 1, 2, 0]
                ],
                [
                    [1, 1, 1, 0],
                    [0, 1, 2, 2]
                ],
                [
                    [0, 1, 1, 1],
                    [0, 0, 1, 2]
                ],
            ]
            pirate = [
                [
                    [0, 1, 1, 2],
                    [0, 0, 1, 1]
                ],
                [
                    [0, 1, 1, 2],
                    [1, 0, 1, 0]
                ],
                [
                    [0, 0, 1, 1],
                    [0, 1, 1, 2]
                ],
                [
                    [1, 0, 1, 0],
                    [0, 1, 1, 2]
                ],
            ]
            # 가로 반전: dy 0 <-> 1
            # 세로 반전: dx 0 <-> 1
            answer = 0
            for x in range(ROW_MAX):
                for y in range(COL_MAX):
                    for type in [warrier, archer, magician, thief, pirate]:
                        for [dx, dy] in type:
                            temp = 0
                            for i in range(4):
                                nx, ny = x + dx[i], y + dy[i]
                                if nx >= ROW_MAX or ny >= COL_MAX or nx < 0 or ny < 0:
                                    temp = 0
                                    break
                                temp += graph[nx][ny]
                            answer = max(answer, temp)
            answers.append(str(answer))
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
        for i in range(1, 3 + 1):
            inputs.append(read_file(f"테트로미노/input{i}.txt"))
            answers.append(read_file(f"테트로미노/output{i}.txt")[0])
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()