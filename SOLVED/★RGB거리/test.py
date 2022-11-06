import unittest


def read_file(filename):
    file = open(filename, "r")
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret


def main(input):
    # # of cases = 3*2**(n-1) == O(2**n)
    n_house = int(input[0])
    dp = [[0] * 3 for _ in range(n_house)]
    cost = []
    for i in range(n_house):
        cost.append(list(map(int, input[1 + i].split(" "))))

    for color in range(3):
        dp[0][color] = cost[0][color]
    for i in range(1, n_house):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + cost[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + cost[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + cost[i][2]
    answer = min(dp[-1])
    print(answer)
    return [str(answer)]


class TestCases(unittest.TestCase):
    def test_input_txt(self):
        input = read_file("RGB거리/input.txt")
        answer = read_file("RGB거리/output.txt")
        self.assertEqual(main(input), answer)


if __name__ == "__main__":
    unittest.main()
