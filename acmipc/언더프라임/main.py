import sys
import math

def num_prime(n):
    ans, div = 0, 2
    while (n >= div):
        if n % div == 0:
            ans += 1
            n /= div
        else:
            div += 1
    return ans

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, max(2, int(math.sqrt(n) + 1))):
        if (n % i) == 0:
            return False
    return True

def main():
    answer = 0
    [A, B] = list(map(int, sys.stdin.readline().split(" ")))
    for i in range(A, B+1):
        if is_prime(num_prime(i)):
            answer += 1
    print(answer)
if __name__ == "__main__":
    main()