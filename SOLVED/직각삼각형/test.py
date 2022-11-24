import unittest

def read_file(filename):
    file = open(filename, 'r')
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret

def main(input):
    i = 0
    tests = []
    while True:
        l = list(map(int, input[i].split()))
        if sum(l) == 0:
            break
        tests.append(sorted(l))
        i += 1
    answer = []
    for a, b, c in tests:
        c2hat = a**2 + b**2
        c2 = c**2
        if c2hat == c2:
            answer.append("right")
        else:
            answer.append("wrong")
    return answer

class TestCases(unittest.TestCase):
    def test_input_txt(self):
        input = read_file('직각삼각형/input1.txt')
        answer = read_file('직각삼각형/output1.txt')
        self.assertEqual(main(input), answer)


if __name__ == '__main__':
    unittest.main()