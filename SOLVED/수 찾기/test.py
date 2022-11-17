import unittest

def read_file(filename):
    file = open(filename, 'r')
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret

def main(input):
    n_given = int(input[0])
    given = set(map(int, input[1].split()))
    n_find = int(input[2])
    to_find = list(map(int, (input[3].split()))) if n_find > 1 else [int(input[3])]
    answer = []
    for i in to_find:
        if i in given:
            print("1")
            answer.append("1")
        else:
            print("0")
            answer.append("0")
    return answer

class TestCases(unittest.TestCase):
    def test_input_txt(self):
        input = read_file('수 찾기/input.txt')
        answer = read_file('수 찾기/output.txt')
        self.assertEqual(main(input), answer)


if __name__ == '__main__':
    unittest.main()