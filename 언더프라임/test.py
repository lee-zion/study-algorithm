import unittest
from traceback import print_exception
import sys, time
from math import isqrt

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
            def num_prime(n):
                # args
                # input  : number to count prime
                # output : n의 소인수 갯수
                ans = 0
                div = 2
                while (n >= div):
                    if n % div == 0:
                        ans += 1
                        n = n // div
                div = 3
                while (n >= div):
                    if n % div == 0:
                        ans += 1
                        n = n // div
                    else:
                        div += 2
                return ans
            def find_divider(n):
                for i in range(1, n // 2 + 1):
                    if (n % (i*2 + 1)) == 0:
                        return i
            # def is_prime(n):
            #     # args
            #     # input  : number to check whether is prime or not
            #     # output : True/False
            #     if n < 2 or n % 2 == 0:
            #         return False
            #     for i in range(3, max(2, isqrt(n) + 1), 2):
            #         if (n % i) == 0:
            #             return False
            #     return True
            
            start = time.perf_counter()

            a, b = map(int, input[0].split())
            answer = 0
            # if dp[i] == 1: i is prime number
            dp = [1] * (b + 1)
            dp[0] = dp[1] = 0
            # to remove if statement inside for loop, ugly repeat occured
            # all even number
            for num in range(2, 3):
                cnt = 2
                while True:
                    temp = num * cnt
                    if temp <= b:
                        dp[temp] = 0
                        cnt += 1
                        continue
                    break
            # all odd number
            for num in range(3, b+1, 2):
                cnt = 2
                while True:
                    temp = num * cnt
                    if temp <= b:
                        dp[temp] = 0
                        cnt += 1
                        continue
                    break
            # IMPORTANT: Compare for-append vs [i for i, e in enumerate if e]
            # dp flaged prime numbers as 1, others as 0
            primes = [i for i, e in enumerate(dp) if e != 0]
            # for di, num in enumerate(dp):
            #     if num:
            #         primes.append(di)
            end = time.perf_counter()
            print(f"Time elapsed: {(end - start)*10**3} ms")
            
            # for i in range(2, b + 1):
            #     if dp[i] == 0:
            #         for j in range(2, b):
            #             if i % j == 0:
            #                 dp[i] = dp[i // j] + 1
            #                 break
            
            # deque.popleft() vs element in list
            for num, is_prime in enumerate(dp[a:b+1]):
                if is_prime:
                    continue
                i_prime = 0
                while True:
                    q, r = divmod(num, primes[i_prime])
                    if r == 0:

                # dp[num] is not prime
                
            answers.append(str(answer))
            end = time.perf_counter()
            print(f"Time elapsed: {(end - start)*10**3} ms")

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
        for i in range(1, 4 + 1):
            inputs.append(read_file(f"언더프라임/input{i}.txt"))
            answers.append(read_file(f"언더프라임/output{i}.txt")[0])
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()