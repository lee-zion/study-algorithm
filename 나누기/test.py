import unittest

def read_file(filename):
    file = open(filename, 'r')
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret

def main(input):
    tabs = []
    for i in range(len(input)):
        tabs.append(list(map(int, input[i].split())))

    s = "is not an integer with less than 100 digits."
    answer = []
    for [t, a, b] in tabs:
        u = f"({t}^{a}-1)/({t}^{b}-1)"
        print(t, a, b)
        num = pow(t, a) - 1
        den = pow(t, b) - 1
        # result is not integer
        if num % den:
            print(f"{u} {s}")
            answer.append(f"{u} {s}")
            continue
        result = num // den
        if len(str(result)) < 100:
            print(f"{u} {result}")
            answer.append(f"{u} {result}")
        else:
            print(f"{u} {s}")
            answer.append(f"{u} {s}")
    return answer
class TestCases(unittest.TestCase):
    def test_input_txt(self):
        input = read_file('나누기/input.txt')
        answer = read_file('나누기/output.txt')
        self.assertEqual(main(input), answer)


if __name__ == '__main__':
    unittest.main()