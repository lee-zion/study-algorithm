import sys

def main():
    n_inset, n_check = map(int, sys.stdin.readline().split())
    s = set()
    [s.add(sys.stdin.readline().strip()) for i in range(n_inset)]
    answer = 0
    for i in range(n_check):
        if sys.stdin.readline().strip() in s:
            answer += 1
    print(answer)
if __name__ == "__main__":
    main()