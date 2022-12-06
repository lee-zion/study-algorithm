import sys
input = sys.stdin.readline
print = sys.stdout.write

def main():
    n = int(input())
    n_max = 10_001
    answer = [0] * n_max
    for _ in range(n):
        answer[int(input())] += 1
    for i in range(1, n_max):
        for _ in range(answer[i]):
            print(str(i) + '\n')