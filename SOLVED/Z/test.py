import unittest

def read_file(filename):
    file = open(filename, 'r')
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret

def main(input):
    [n, r, c] = list(map(int, input[0].split(" ")))
    offset = 0
    while (n > 1):
        det, adder = 2**(n-1), 4**(n-1)
        if r < det:
            if c < det:
                None
            else:
                offset += adder
                c -= det
        else:
            if c < det:
                offset += adder*2
                r -= det
            else:
                offset += adder*3
                r -= det
                c -= det
        n -= 1
        if n == 1:
            offset += 2*r + c
    return offset

class TestCases(unittest.TestCase):
    def test_input_txt(self):
        input = read_file('Z/input.txt')
        answer = read_file('Z/output.txt')
        self.assertEqual(main(input), answer)

        # input = read_file('Z/input.txt')
        # answer = read_file('Z/input.txt')
        # for d in input:
        #     [n, r, c] = list(map(int, d.split(" ")))
        #     print(n, r, c, answer)
        #     self.assertEqual(main(n, r, c), answer)


if __name__ == '__main__':
    unittest.main()