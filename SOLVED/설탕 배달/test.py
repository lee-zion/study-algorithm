import unittest

def read_file(filename):
    file = open(filename, 'r')
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret

def main(input):
    answer = 0
    candidates = [5, 3]
    target = int(input[0])
    while target > 0:
        if target%candidates[0] == 0:
            answer += target // candidates[0]
            break
        else:
            target -= candidates[1]
            answer += 1
    if target < 0:
        return ["-1"]
    return [str(answer)]

class TestCases(unittest.TestCase):
    def test_input_txt(self):
        input = read_file('설탕 배달/input.txt')
        answer = read_file('설탕 배달/output.txt')
        self.assertEqual(main(input), answer)


if __name__ == '__main__':
    unittest.main()