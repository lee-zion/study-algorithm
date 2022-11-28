import unittest
from traceback import print_exception
import sys
from math import log2, pow, isqrt

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
            answer = []
            T = int(input[0])
            for i in range(T):
                depart, dest = map(int, input[1+i].split())
                # depart~dest의 이동은 반드시 대칭을 이룰 것
                # 
                diff = dest - depart
                # 2**n <= diff < 2**(n+1)을 만족하는 n 찾기
                iroot = isqrt(diff)
                log2n = int(log2(diff))
                root2 = pow(iroot, 2)
                if diff == root2:
                    answer.append(str(2*iroot - 1))
                    # print(2*root - 1)
                elif diff <= root2 + iroot:
                    answer.append(str(2*iroot))
                    # print(2*root)
                else:
                    answer.append(str(2*iroot + 1))
                    # print(2*root - 1)
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
            inputs.append(read_file(f"Fly me to the Alpha Centauri/input{i}.txt"))
            answers.append(read_file(f"Fly me to the Alpha Centauri/output{i}.txt"))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()