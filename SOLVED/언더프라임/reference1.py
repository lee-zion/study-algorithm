# https://www.acmicpc.net/source/51340663
# 32404 kb, 124 ms
import sys

# underscore _ is a visual seperator
MAX = 100_004 

def get_ints():
    return tuple(int(x) for x in sys.stdin.readline().strip().split())

# 에라토스테네스의 체
def sieve():
    # [2, 0]을 총 (MAX // 2 == MAX >> 1)번 반복
    res = [2, 0] * (MAX >> 1)

    # 3부터 최대 숫자까지의 모든 홀수만 체에 거른다
    # for p in range(3, math.isqrt(MAX) + 1), 2):
    for p in range(3, int(MAX ** .5 + 1), 2):
        # 3 이상, isqrt(MAX) 이하의 모든 홀수가 해당
        if res[p] == 0:
            # p*3부터 MAX 이하 범위, 매 반복마다 p 2배 증가
            for i in range(p * 3, MAX, p << 1):
                res[i] = p
    # 0, 1, 2는 0 (?/) 
    res[:3] = 0, 0, 0
    # res = [0, 0, 0, p?0?, 2, p?0?, 2, ...]
    return res

s = sieve()

def is_underprime(x: int):
    # 판정할 수 x를 입력
    num = 1
    while x > 1 and s[x]:
        x //= s[x]
        num += 1
    return num > 1 and s[num] == 0

def main():
    a, b = get_ints()
    print(sum([is_underprime(x) for x in range(a, b+1)]))

main()