import unittest
from traceback import print_exception
import sys
from functools import reduce
from itertools import combinations

def read_file(filename):
    file = open(filename, 'r')
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret

def main(inputs):
    answers = []
    try:
        for input in inputs:
            """
            """
            # your code here
            n_problem, n_mate = map(int, input[0].split())
            all_solved = 2**n_problem - 1
            abilities = dict()
            for i in range(n_mate):
                l = list(map(int, input[1+i].split()))[1:]
                solvable = 0
                for e in l:
                    solvable += 2**(e-1)
                abilities[i+1] = solvable
            answer = -1
            def find_dreamteam(comb_candidates):
                nonlocal answer, n_mate, all_solved, abilities
                for candidates in comb_candidates:
                    temp = 0
                    for candidate in candidates:
                        temp |= abilities[candidate]
                    if temp == all_solved:
                        return len(candidates)
                return -1
                
            for k in range(1, n_mate + 1):
                comb_candidates = combinations([i for i in range(1, n_mate + 1)], k)
                answer = find_dreamteam(comb_candidates)
                if answer != -1:
                    break
            answers.append(answer)
        return answers
    except Exception:
        print(f"===========================================================================")
        print(f"Failed in the case below")
        print(f"input: {input}")
        exc_info = sys.exc_info()
        print_exception(*exc_info)
        print(f"===========================================================================")
        del exc_info
class TestCases(unittest.TestCase):
    def test_input_txt(self):
        inputs, answers = [], []
        for i in range(1, 1 + 1):
            inputs.append(read_file(f"팀원 모집/input{i}.txt"))
            answers.append(int(read_file(f"팀원 모집/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()