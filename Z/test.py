import unittest

def read_file(filename):
    file = open(filename, 'r')
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret

def main(n, r, c):
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
        data = read_file('acmipc/Z/input.txt')
        for d in data:
            [n, r, c, answer] = list(map(int, d.split(" ")))
            print(n, r, c, answer)
            self.assertEqual(main(n, r, c), answer)


if __name__ == '__main__':
    unittest.main()