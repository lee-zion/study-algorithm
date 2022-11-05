import unittest, sys
from collections import deque


def read_file(filename):
    file = open(filename, "r")
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret

def main(input):
    target = int(input[0])
    dp = [0] * target
    for i in range(1, target):
        dp[i] = dp[i - 1] + 1
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
    print(dp[-1])
    return [str(dp[-1])]

class TestCases(unittest.TestCase):
    def test_input_txt(self):
        input = read_file("1로 만들기/input.txt")
        answer = read_file("1로 만들기/output.txt")
        self.assertEqual(main(input), answer)


if __name__ == "__main__":
    unittest.main()
