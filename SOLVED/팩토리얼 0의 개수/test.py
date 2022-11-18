import unittest, time

def read_file(filename):
    file = open(filename, 'r')
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret

def main(input):
    start = time.perf_counter()
    n = int(input[0])
    n_int = 1
    for i in range(1, n+1):
        n_int *= i
    n_str = str(n_int)
    target = "0"
    answer = 0
    for i in range(len(n_str) - 1, -1, -1):
        if n_str[i] != target:
            break
        answer += 1
    end = time.perf_counter()
    print(f"Time elapsed: {(end - start)*10**3} ms")
    return [str(answer)]

class TestCases(unittest.TestCase):
    def test_input_txt(self):
        input = read_file('팩토리얼 0의 개수/input.txt')
        answer = read_file('팩토리얼 0의 개수/output.txt')
        self.assertEqual(main(input), answer)

if __name__ == '__main__':
    unittest.main()