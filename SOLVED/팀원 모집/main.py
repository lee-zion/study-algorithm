import sys
from itertools import combinations
input = sys.stdin.readline

def main():
    n_problem, n_mate = map(int, input().strip().split())
    all_solved = 2**n_problem - 1
    abilities = dict()
    for i in range(n_mate):
        l = list(map(int, input().strip().split()))[1:]
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
    print(answer)

if __name__ == "__main__":
    main()