import unittest
from traceback import print_exception
import sys, math, itertools

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
            answer = True
            for t in range(int(input[0])):
                # https://sgc109.tistory.com/89
                # https://suuntree.tistory.com/187
                # https://justicehui.github.io/icpc/2019/02/10/BOJ9359/
                #
                # n의 소인수분해: n = a1 x a2 x ... x an
                # n의 서로소 = 전체 수 - a1의 배수 - a2의 배수 - ... - an의 배수 + (a1과 a2의 배수) + (a1과 a3의 배수) + ... + (an-1과 an의 배수) - (a1과 a2와 a3의 배수) - (a1과 a2와 a4의 배수) - ... - (an-2과 an-1과 an의 배수) + ... - ... + (-1)^(확인하는 숫자의 수 - 1) (a1과 a2와 ...과 an의 배수)
                def factorize_prime(n):
                    # args
                    # input  : number to count prime
                    # output : n의 소인수 갯수
                    sqrt = math.isqrt(n) + 1
                    div = 2
                    answer = set()
                    while div <= sqrt:
                        if n % div == 0:
                            n = n // div
                            answer.add(div)
                        else:
                            div += 1
                    return list(answer)
                
                def get_multiple(n, base):
                    return n // base
                
                a, b, n = map(int, input[1+t].split())
                n_list = factorize_prime(n)
                
                # for nC1 + nC2 + ... + nCn = 2^n - 1
                for i in range(1, n):
                    temp = itertools.combinations(n_list, i)
                    for ic in temp:
                        mul = 1
                        for icc in ic:
                            mul *= icc
                        get_multiple(mul, )
                answer = f"Case #{t}: "
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
            inputs.append(read_file(f"서로소/input{i}.txt"))
            answers.append(read_file(f"서로소/output{i}.txt"))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()