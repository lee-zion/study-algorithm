import unittest

def read_file(filename):
    file = open(filename, 'r')
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret

def main(input):
    def bin_flip(str):
        ret = ""
        for s in str:
            ret += "1" if s == "0" else "0"
        return ret
    
    def find_nth(haystack, needle, n):
        start = haystack.find(needle)
        while start >= 0 and n > 1:
            start = haystack.find(needle, start + len(needle))
            n -= 1
        return start

    # capability : maximum 1's
    # cnt        : current 1's
    bottle, k = map(int, input[0].split())
    bottle_bin = bin(bottle)[2:]

    # find k'th "1" == ik
    # 수 x 찾기
    # x는 bottle_bin[ik:] + x = 100...00 (count("0") == len(bottle_bin[ik:]))를 만족
    # ik부터 flip하고 마지막 1부터는 그대로
    # ex) 00 0010 0100 0000
    #  -> 11 1101 1100 0000

    if bottle_bin.count("1") <= k:
        answer = 0
    else:
        ik = find_nth(bottle_bin, "1", k) + 1
        ilast = bottle_bin.rfind("1")
        x = bin_flip(bottle_bin[ik:ilast]) + bottle_bin[ilast:]
        # bottle_bin[:ik] == "1..1" <-- total k of "1"s
        # bottle_bin[ik:] == "0..1.." <-- 
        answer = int(x, 2)
    return [str(answer)]

class TestCases(unittest.TestCase):
    def test_input_txt(self):
        input = read_file('물병/input3.txt')
        answer = read_file('물병/output3.txt')
        self.assertEqual(main(input), answer)


if __name__ == '__main__':
    unittest.main()