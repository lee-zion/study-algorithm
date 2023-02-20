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
            """
            nC1 + nC2 + ... + nCn =??
            
            1*10
            
            1*8+2*1
            1*6+2*2
            1*4+2*3
            1*2+2*4
            
            1*5+5*1
            
            5*1+2*2+1*1
            5*1+2*1+1*3
            
            2*5
            5*2

            dp[i][j] :== 총 i개의 동전?으로 가치 j를 만들 수 있는 경우의 수
            """
            # your code here
            n, target = map(int, input[0].split())
            values = []
            for i in range(n):
                values.append(int(input[1+i]))
            answer = 0
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
            inputs.append(read_file(f"동전 1/input{i}.txt"))
            answers.append(int(read_file(f"동전 1/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()