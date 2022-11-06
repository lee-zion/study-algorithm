import unittest

def read_file(filename):
    file = open(filename, 'r')
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret

def main(input):
    return True

class TestCases(unittest.TestCase):
    def test_input_txt(self):
        input = read_file('케빈 베이컨의 6단계 법칙/input.txt')
        answer = read_file('케빈 베이컨의 6단계 법칙/output.txt')
        self.assertEqual(main(input), answer)


if __name__ == '__main__':
    unittest.main()