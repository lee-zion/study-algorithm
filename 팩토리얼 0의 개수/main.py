import sys

def main():
    n = int(sys.stdin.readline())
    n_int = 1
    for i in range(1, n+1):
        n_int *= i
    n_str = str(n_int)
    target = "0"
    answer = 0
    for i in range(len(n_str) - 1, -1, -1):
        if n_str[i] != target:
            break
        answer += 1
    print(answer)

if __name__ == "__main__":
    main()