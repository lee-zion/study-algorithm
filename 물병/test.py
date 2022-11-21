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

    bottle_bin.count("1")

    # find index of first "0" === i0
    # if i0 < k:
    # check if "1" exists after i0
    # if "1" in bottle[i0:]:
    #   must add some number
    #

    
    # bin(str) to int       
    # bin(int,2) to int     
    # int,10 to bin(int,2)  
    # int,10 to bin(str)    bin()
    # answer = []
    # # count continuous 1's from bottle_bin
    # cnt, i_cnt = 0, 0
    # for i, b in enumerate(bottle_bin):
    #     if b == '1':
    #         cnt += 1
    #     else:
    #         i_cnt = i
    #         break
    # no_ones = True
    # for i in bottle_bin[i_cnt:]:
    #     if i == "1":
    #         no_ones = False
    #         break
    # # ending condition
    # # if cnt <= capability and no_ones:
    return True

class TestCases(unittest.TestCase):
    def test_input_txt(self):
        input = read_file('물병/input3.txt')
        answer = read_file('물병/output3.txt')
        self.assertEqual(main(input), answer)


if __name__ == '__main__':
    unittest.main()