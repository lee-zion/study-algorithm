import unittest
from traceback import print_exception
import sys, itertools

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
            n, m = map(int, input[0].split())
            nums = [str(i) for i in range(1, n+1)]
            # answer = []
            # def permutation(temp):
            #     nonlocal nums, m, answer
            #     for num in nums:
            #         temp += num
            #         if len(temp) < m:
            #             permutation(temp)
            #             temp = temp[:-1]
            #         else:
            #             answer.append(' '.join(sorted(temp, key=int)))
            #             temp = temp[:-1]
            # permutation("")
            # answers.append(list(dict.fromkeys(answer)))
            comb = itertools.combinations_with_replacement(sorted(nums, key=int), m)
            answer = []
            for i in list(dict.fromkeys(comb)):
                answer.append(' '.join(i))
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
        for i in range(1, 3 + 1):
            inputs.append(read_file(f"731d3d782f6f712c4001b5eddcc5c200ff3610e5/input{i}.txt"))
            answers.append(read_file(f"731d3d782f6f712c4001b5eddcc5c200ff3610e5/output{i}.txt"))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()