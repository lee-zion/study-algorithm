import unittest

def read_file(filename):
    file = open(filename, 'r')
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret

def main(input):
    answer = []
    n_test = int(input[0])
    n_case = []
    
    for i in range(n_test):
        n_case.append(int(input[1+i]))
    
    def fib(stack, curr):
        now = stack[curr]
        stack[curr] = 0
        stack[curr - 1] += now
        stack[curr - 2] += now

    for case in n_case:
        stack = [0]*(case + 1) if case > 0 else [0]*2
        curr = case
        stack[curr] = 1
        while curr > 1:
            fib(stack, curr)
            curr -= 1
        # answer.append(stack[:2])
        answer.append(" ".join(map(str, stack[:2])))
    return answer

class TestCases(unittest.TestCase):
    def test_input_txt(self):
        input = read_file('피보나치 함수/input.txt')
        answer = read_file('피보나치 함수/output.txt')
        self.assertEqual(main(input), answer)


if __name__ == '__main__':
    unittest.main()