import unittest
from traceback import print_exception
import sys
import math

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
            1) N 이상 소수 판별
            2) N 이상 팰린드롬 판별
            s = str(N)
            n = len(s)
            mid = n // 2 # 4 -> 2, 5 -> 2
            s[:mid] == s[mid+1::-1]

            소수가 많을까 펠린드롬 수가 많을까?
            소수판별이 빠를까 펠린드롬 판별이 빠를까?
            펠린드롬이 빠름. 따라서 소수를 먼저 판별하고 펠린드롬 판별을 해야함.
            """
            def is_prime(n: int):
                if n == 1:
                    return False
                for i in range(2, math.ceil(math.sqrt(n)) + 1):
                    if n % i == 0:
                        return False
                return True
            def is_palindrome(n: int):
                s = str(n)
                n = len(s)
                mid = n // 2
                return s[:mid] == s[:mid:-1]
            l = [1661, 1771, 1881, 1991, 3113, 3223, 3443, 3553, 3773, 3883, 7117, 7227, 7337, 7447, 7557, 7667, 7887, 7997, 9119, 9229, 9339, 9449, 9559, 9669, 9779, 9889]
            for e in l:
                print(e, is_prime(e))
            answer = False
            MAX = 1_000_000
            # for n in range(int(input[0]), MAX + 1):
            for n in range(1000, MAX + 1):
                if is_prime(n):
                    if is_palindrome(n):
                        answer = n
                        break
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
            inputs.append(read_file(f"소수&팰린드롬/input{i}.txt"))
            answers.append(int(read_file(f"소수&팰린드롬/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()