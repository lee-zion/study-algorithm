import unittest
from math import comb

def read_file(filename):
    file = open(filename, 'r')
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret

def main(input):
    T = int(input[0])
    answer = []
    for t in range(T):
        n, m = map(int, input[1+t].split())
        answer.append(str(comb(m, n)))
    return answer

class TestCases(unittest.TestCase):
    def test_input_txt(self):
        input = read_file('다리 놓기/input1.txt')
        answer = read_file('다리 놓기/output1.txt')
        self.assertEqual(main(input), answer)


if __name__ == '__main__':
    unittest.main()