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
            # your code here
            # max가 여러명인 경우
            # +1하기
            # 이전까지는?
            # max를 찾아서 diff의 절반만큼 (홀수인 경우 +1) 매수
            votes = []
            for i in range(int(input[0])):
                votes.append(int(input[1+i]))
            answer = 0
            while True:
                M = max(votes)
                iM = votes.index(M)
                if iM == 0:
                    # if there are multiple of vote M
                    if votes[::-1].index(M) != len(votes) - 1:
                        answer += 1
                    break
                # votes를 뒤집어서 iM이 바뀐다면, M이 여러개 있다는 것.
                # divmod의 2nd arg를 M의 갯수로 바꿔야 할듯?
                # 0 10 ... 10을 못 푸는 이유가 이건데?
                q, r = divmod(M - votes[0], 2)
                diff = q + r
                votes[0] += diff
                votes[iM] -= diff
                answer += diff
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
        for i in range(6, 6 + 1):
            inputs.append(read_file(f"국회의원 선거/input{i}.txt"))
            answers.append(int(read_file(f"국회의원 선거/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()