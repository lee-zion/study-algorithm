# EM Pattern = (100+1+ | 01)+
# basis vector of vega space = { 01, 100+1+ }
# -> check if string can be parsed to 01 or 100+1+
import re
import sys
def main():
    num_cases = int(sys.stdin.readline())
    cases_input = []
    for i in range(num_cases):
        cases_input.append(sys.stdin.readline().strip())
    cases_answer = [0]*num_cases

    for i, case_input in enumerate(cases_input):
        if len(case_input) < 6:
            cases_answer[i] = 'NO'
            continue
        pattern='(100+1+|01)+'
        if re.fullmatch(pattern, case_input):
            cases_answer[i] = 'YES'
        else:
            cases_answer[i] = 'NO'
    print(cases_answer)
    return

if __name__ == '__main__':
    main()