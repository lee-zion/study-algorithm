import unittest

def read_file(filename):
    file = open(filename, 'r')
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret

def main(input):
    # 1. 중앙 기준 양쪽 구슬 개수 차이 최소화
    # 2. 구슬 개수 총합 최대화
    # 3. 구슬 무게 총합 최대화
    # 4. 양쪽 구슬 좌측부터 순서대로
    # 가장 높은 점수의 구슬 배열 반환
    answers = []
    n = len(input)
    for i in range(n):
        
    return True

class TestCases(unittest.TestCase):
    def test_input_txt(self):
        input = [1,2,3,4,4]
        answer = [1,4,4,2,3]
        
        self.assertEqual(main(input), answer)


if __name__ == '__main__':
    unittest.main()