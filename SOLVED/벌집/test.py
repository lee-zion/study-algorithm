import unittest
from traceback import print_exception
import sys, string

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
            # input	    output	increment
            # [1]	    1	    -
            # [2, 7]	2	    +1
            # [8, 19]	3	    +6 = 6*1
            # [20, 37]	4	    +12 = 6*2
            # [38, 61]	5	    +18 = 6*3
            # [62, 85]	6	    +24 = 6*4
            # [86, 115]	7	    +30 = 6*5
            # [a, b]	n	    +<b-a+1> = 6 * <n-2>

            # tmp = string.digits+string.ascii_lowercase
            # def convert(num, base) :
            #     q, r = divmod(num, base)
            #     if q == 0 :
            #         return tmp[r] 
            #     else :
            #         return convert(q, base) + tmp[r]

            # # 껍질의 깊이에 따른 길이를 수열로 표현하면
            # # 최대 10억
            # # 깊이  1, 2,  3,  4,  5, ...
            # # 길이  1, 6, 12, 18, 24, ...
            # num = int(input[0])
            # answer = None
            # i_num = num - 1 / 6
            # for n in range(1, 10**9):
            #     an_prev = n*(n-1) / 2
            #     an_curr = n*(n+1) / 2
            #     if an_prev < num <= an_curr:
            #         answer = n - 2
            #         break

            answer, acc = 1, 1
            n = int(sys.stdin.readline())
            while n > acc:
                acc += 6 * answer
                answer += 1
            
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
        for i in range(1, 1 + 1):
            inputs.append(read_file(f"벌집/input{i}.txt"))
            answers.append(read_file(f"벌집/output{i}.txt")[0])
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()