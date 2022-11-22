import unittest

def read_file(filename):
    file = open(filename, 'r')
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret

def main(input):
    # 규칙
    # 시작끝 숫자
    # 연속 연산자 X
    # 5자리 이하의 숫자
    # 0으로 시작 가능
    # 총 길이 50 이하
    # test case 4, 5 실패
    # 235235+034674 같은 경우를 처리하지 못함 (+에 0이 붙은 경우)
    eqn = input[0]
    eqn_minus = eqn.split("-")
    for i in range(len(eqn_minus)):
        if eqn_minus[i][0] == "0":
            # find the first index of non-zero element
            ix = next((i for i, x in enumerate(eqn_minus[i]) if int(x)), None)
            if ix:
                eqn_minus[i] = eqn_minus[i][ix:]
            else:
                # if all elements are zero, replace with 0
                eqn_minus[i] = "0"
    answer = eval(eqn_minus[0])
    if len(eqn_minus) > 1:
        for eqn_part in eqn_minus[1:]:
            eqn_plus = eqn_part.split("+")
            if len(eqn_plus) > 1:
                for i in range(len(eqn_plus)):
                    if eqn_plus[i][0] == "0":
                        ix = next((i for i, x in enumerate(eqn_plus[i]) if int(x)), None)
                        eqn_plus[i] = eqn_plus[i][ix:] if ix else "0"
                    answer -= eval(eqn_plus[i])
            else:
                answer -= eval(eqn_part)
    return [str(answer)]

class TestCases(unittest.TestCase):
    def test_input_txt(self):
        tn = 3
        input = read_file(f'잃어버린 괄호/input{tn}.txt')
        answer = read_file(f'잃어버린 괄호/output{tn}.txt')
        self.assertEqual(main(input), answer)


if __name__ == '__main__':
    unittest.main()