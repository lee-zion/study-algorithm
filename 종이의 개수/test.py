import unittest
from traceback import print_exception
import sys, math


def read_file(filename):
    file = open(filename, "r")
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
            k = int(math.log(n, 3))
            paper = []
            for i in range(n):
                paper.append(list(map(int, input[1 + i].split())))
            counted = {0: 0, 1: 0, -1: 0}

            def cut_paper(paper, heart, step):
                nonlocal counted, n
                if heart == 0:
                    counted[paper[0][0]] += 1
                else:
                    for x in range(3):
                        for y in range(3):
                            sx, sy = step * x, step * y
                            subpaper = [
                                row[sy : sy + step] for row in paper[sx : (sx + step)]
                            ]
                            is_all_same = True
                            for row in subpaper:
                                if not all(i == row[0] for i in row):
                                    is_all_same = False
                                    break
                            if is_all_same:
                                counted[subpaper[0][0]] += 1
                            else:
                                cut_paper(subpaper, heart - 1, step // 3)

            cut_paper(paper, k, n // 3)
            for key in range(-1, 2):
                answers.append(counted[key])
        return answers
    except Exception:
        print(
            f"==========================================================================="
        )
        print(f"Failed in the case below")
        print(f"input: {input}")
        exc_info = sys.exc_info()
        print_exception(*exc_info)
        print(
            f"==========================================================================="
        )
        del exc_info


class TestCases(unittest.TestCase):
    def test_input_txt(self):
        inputs, answers = [], []
        for i in range(2, 2 + 1):
            inputs.append(read_file(f"종이의 개수/input{i}.txt"))
            answers.append(read_file(f"종이의 개수/output{i}.txt"))
        self.assertEqual(main(inputs), list(map(int, answers[0])))


if __name__ == "__main__":
    unittest.main()
