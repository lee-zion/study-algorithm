import unittest

def read_file(filename):
    file = open(filename, 'r')
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret

def main(input):
    # capability : maximum continuous 1's
    # cnt        : current continuous 1's
    # if current <= capability
    bottle, capability = map(int, input[0].split())
    bottle_bin = bin(bottle)[2:]
    # get desired minimum
    desired = ""
    for i in range(capability):
        desired += "1"
    
    answer = []
    # count continuous 1's from bottle_bin
    cnt, i_cnt = 0, 0
    for i, b in enumerate(bottle_bin):
        if b == '1':
            cnt += 1
        else:
            i_cnt = i
            break
    no_ones = True
    for i in bottle_bin[i_cnt:]:
        if i == "1":
            no_ones = False
            break
    # ending condition
    # if cnt <= capability and no_ones:
    return True

class TestCases(unittest.TestCase):
    def test_input_txt(self):
        input = read_file('물병/input1.txt')
        answer = read_file('물병/output1.txt')
        self.assertEqual(main(input), answer)


if __name__ == '__main__':
    unittest.main()