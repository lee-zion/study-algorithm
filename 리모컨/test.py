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
    brokens = list(map(int, input[2].split(" ")))
    candidates = list(range(10))
    for i, broken in enumerate(brokens):
        del candidates[broken - i]
    
    answer = 5*10**5
    channel = ""
    def dfs(channel):
        nonlocal answer, target, candidates
        for btn in candidates:
            channel += str(btn)
            answer = min(answer, abs(int(channel) - target) + len(channel))
            if len(str(channel)) < len(str(target)) + 1:
                dfs(channel)
            else:
                channel = channel[:-1]
    dfs(channel)


    answer = min(answer + abs(answer - target), abs(answer - begin))
    # for power in range(len(target)):
    #     digit = target[-power-1]
    # # for power, digit in enumerate(target):
    #     dist = []
    #     digit = int(digit)
    #     for cand in candidates:
    #         if cand > digit:
    #             dist.append(cand - digit)
    #         else:
    #             dist.append(digit - cand)
    #     # find the index of minimum value
    #     val, idx = min((val, idx) for (idx, val) in enumerate(dist))
    #     answer += candidates[idx] * 10**power

    return True


class TestCases(unittest.TestCase):
    def test_input_txt(self):
        input = read_file("리모컨/input.txt")
        answer = read_file("리모컨/output.txt")
        self.assertEqual(main(input), answer)


if __name__ == "__main__":
    unittest.main()
