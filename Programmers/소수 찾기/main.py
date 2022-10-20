from itertools import permutations

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, 1+(-((-num)//2))):
        if num%i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    candidates = []
    
    # make candidate list
    for i in range(1, len(numbers)+1):
        candidates += list(map(int, map(''.join, permutations(numbers, i))))
    
    # to avoid duplicated in list, use set
    candidates = list(set(candidates))
        
    # run function `is_prime` for candidates
    for candidate in candidates:
        if is_prime(int(candidate)):
            answer += 1
    return answer