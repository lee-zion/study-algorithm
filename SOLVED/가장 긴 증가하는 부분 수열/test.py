import unittest
from traceback import print_exception
import sys
from bisect import bisect_left

def read_file(filename):
    file = open(filename, 'r')
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret

def main(inputs):
    try:
        answers = []
        for input in inputs:
            # your code here
            """
            Longest Increasing Subsequence
            https://chanhuiseok.github.io/posts/algo-49/

            Maximum Subarray problem
            https://modoocode.com/247
            """

            def lis_n2(seq: list):
                ls = len(seq)
                lis = [0] * ls
                for i in range(ls):
                    lis[i] = 1
                    for j in range(i):
                        if seq[i] > seq[j]:
                            lis[i] = max(lis[i], lis[j] + 1)
                return lis
            
            def binary_search(left: int, right: int, seq: list, dest: int):
                while left < right:
                    mid = (left + right) >> 1
                    if seq[mid] >= dest:
                        right = mid
                    else:
                        left = mid + 1
                return right
            def lis_nlogn(seq: list):
                """
                binary search reduces n to log n
                for j in range(i) -> bin_search
                """
                ls = len(seq)
                lis = [seq[0]]
                for i in range(1, ls):
                    if seq[i] < lis[-1]:
                        # binary search in seq to find index
                        # why no heap?
                        # -> lis must be able to update i-th element, where heap should pop and push all the i-1 elements to update
                        idx = binary_search(0, len(lis), lis, seq[i])
                        lis[idx] = seq[i]
                    elif seq[i] > lis[-1]:
                        lis.append(seq[i])
                return lis
            
            def lis_nlogn_bisect(seq: list):
                ls = len(seq)
                lis = [seq[0]]
                for i in range(1, ls):
                    if seq[i] < lis[-1]:
                        idx = bisect_left(lis, seq[i])
                        lis[idx] = seq[i]
                    elif seq[i] > lis[-1]:
                        lis.append(seq[i])
                return lis
            n = int(input[0])
            nums = list(map(int, input[1].split()))
            # answer = lis_n2(nums)
            # answers.append(max(answer))
            # answer = lis_nlogn(nums)
            # answers.append(len(answer))
            answer = lis_nlogn_bisect(nums)
            answers.append(len(answer))
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
            inputs.append(read_file(f"가장 긴 증가하는 부분 수열/input{i}.txt"))
            answers.append(int(read_file(f"가장 긴 증가하는 부분 수열/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()