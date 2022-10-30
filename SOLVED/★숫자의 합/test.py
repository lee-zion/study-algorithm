import unittest

def read_file(filename):
    file = open(filename, 'r')
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret

def main(input):
    [l, num] = input
    sum = 0
    for i in range(int(l)):
        sum += int(num[i])
    return [str(sum)]

class TestCases(unittest.TestCase):
    def test_input_txt(self):
        input = read_file('숫자의 합/input.txt')
        answer = read_file('숫자의 합/output.txt')
        self.assertEqual(main(input), answer)


if __name__ == '__main__':
    unittest.main()