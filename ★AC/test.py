import unittest
from collections import deque

def read_file(filename):
    file = open(filename, 'r')
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret

def main(input):
    n_test = int(input[0]) + 1
    offset = 0
    answer = []
    for i in range(1, n_test):
        commands = input[offset + 1]
        merged = input[offset + 3].strip("[").strip("]")
        arr = []
        if merged != "":
            arr = list(map(int, merged.split(",")))
        offset += 3
        q = deque(arr)
        is_reversed = False
        for cmd in commands:
            if cmd == "R":
                is_reversed = not is_reversed
            elif cmd == "D":
                if not q:
                    answer.append("error")
                elif is_reversed:
                    q.pop()
                else:
                    q.popleft()
        arr = list(q)
        if is_reversed:
            arr.reverse()
        # ret = "[" + ",".join(map(str, arr)) + "]"
        ret = f'[{",".join(map(str, arr))}]'
        # ret = f'[{",".join(list(q))}]'
        answer.append(str(ret))
    return answer

class TestCases(unittest.TestCase):
    def test_input_txt(self):
        input = read_file('★AC/input.txt')
        answer = read_file('★AC/output.txt')
        self.assertEqual(main(input), answer)


if __name__ == '__main__':
    unittest.main()