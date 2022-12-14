import unittest
from traceback import print_exception
import sys


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
            cnt = {}
            arith_mean = 0
            for i in range(n):
                num = int(input[1 + i])
                arith_mean += num
                cnt[num] = cnt[num] + 1 if num in cnt else 1
            arith_mean = round(arith_mean / n)
            median = -1
            acc = 0
            for i, key in enumerate(sorted(cnt.keys())):
                acc += cnt[key]
                if acc <= n // 2:
                    continue
                median = key
                break
            val_max = max(cnt.values())

            max_nominee = []
            for i, key in enumerate(sorted(cnt.keys())):
                if cnt[key] == val_max:
                    max_nominee.append(key)
            frequent = max_nominee[1] if len(max_nominee) > 1 else max_nominee[0]
            dist = max(cnt.keys()) - min(cnt.keys())
            answer = [str(arith_mean), str(median), str(frequent), str(dist)]
            print(arith_mean)
            print(median)
            print(frequent)
            print(dist)
            answers.append(answer)
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
        for i in range(1, 4 + 1):
            inputs.append(read_file(f"통계학/input{i}.txt"))
            answers.append(read_file(f"통계학/output{i}.txt"))
        self.assertEqual(main(inputs), answers)


if __name__ == "__main__":
    unittest.main()
