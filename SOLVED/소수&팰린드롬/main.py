import sys
import math
input = sys.stdin.readline

def main():
    n = int(input().strip())

    def is_prime(n: int):
        if n == 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        
        for i in range(2, math.ceil(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    def is_palindrome(n: int):
        s = str(n)
        return s == s[::-1]
    for n in range(n, 2_000_001):
        if is_palindrome(n):
            if is_prime(n):
                print(n)
                return

if __name__ == "__main__":
    main()