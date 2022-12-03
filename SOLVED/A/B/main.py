import sys

def main():
    a, b = map(int, sys.stdin.readline().rstrip().split())
    answer_true = a / b
    answer, x = None, 0.1
    while True:
        x = x * (2 - b * x)
        answer = x * a
        diff_abs = abs(answer - answer_true)
        diff_rel = diff_abs / answer_true * 100
        precision = 10**-9
        if diff_abs <= precision or diff_rel <= precision:
            break
    print(answer)

    # a, b = map(int, sys.stdin.readline().rstrip().split())
    # print(a / b)

if __name__ == "__main__":
    main()