# EM Pattern = (100+1+ | 01)+
# 합집합의 반복
# 합집합
# 10 (0..0) (1..1) | 01
# min: 1001 01 01 1001
# max: 10 0..0 1..1 01
#      01 10 0..0 1..1
import os

def readFile(filename):
    script_dir = os.path.dirname(__file__)
    path_to_file = os.path.join(script_dir, filename)
    file = open(path_to_file, 'r')
    ret = file.readlines()
    for line in range(len(ret)):
        ret[line] = ret[line].strip()
    file.close()
    return ret

def main(*args, **kwargs):
    file_raw = readFile("input.txt")
    num_cases = file_raw[0]
    cases_input = []
    for i in range(int(num_cases)):
        cases_input.append(file_raw[i+1])
    print(cases_input)

    for case_input in cases_input:
        # if pattern matches with
        # 10 0..0 1..1 01
        # or
        # 0110 0..0 1..1
        case_input

if __name__ == '__main__':
    main()