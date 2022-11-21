import unittest


def read_file(filename):
    file = open(filename, "r")
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret


def main(input):
    begin = 100
    target = int(input[0])
    n_broken = int(input[1])
    candidates = set(range(10))
    if n_broken:
        candidates = list(candidates.symmetric_difference(set(map(int, input[2].split()))))
    
    answer = 5*10**5
    channel = ""
    def dfs(channel):
        nonlocal answer, target, candidates
        for btn in candidates:
            channel += str(btn)
            answer = min(answer, abs(int(channel) - target) + len(channel))
            if len(str(channel)) < 6:
                dfs(channel)
                channel = channel[:-1]
            else:
                channel = channel[:-1]
    dfs(channel)
    answer = min(answer, abs(target - begin))
    return [str(answer)]

class TestCases(unittest.TestCase):
    def test_input_txt(self):
        input = read_file("리모컨/input.txt")
        answer = read_file("리모컨/output.txt")
        self.assertEqual(main(input), answer)


if __name__ == "__main__":
    unittest.main()
