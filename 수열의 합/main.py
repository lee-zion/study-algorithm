import sys

# N, L
# N: Sum of elements
# L: Minimum number of elements
# sum_i=[a, b] -> 
# sum from 1 to n = n(n+1)/2 
# sum from a to b = sum from 1 to b - sum from 1 to a
# N = (b*b + b - a*a - a)/2
# L = b - a + 1

def main():
    [N, L] = list(map(int, sys.stdin.readline().split(" ")))
    print(N, L)
    MAX = 1000000000
    ans = []
    for a in range(1, MAX):
        for b in range(a + L - 1, MAX):
            b = a + L - 1
            sum_a = (a*a + a) / 2
            sum_b = (b*b + b) / 2
            if (sum_b - sum_a == N):
                for i in range(a, b):
                    ans.append(i)
                break
            elif (sum_b - sum_a > N):
                break
        if a == MAX:
            ans.append(-1)
    print(ans)


if __name__ == "__main__":
    main()