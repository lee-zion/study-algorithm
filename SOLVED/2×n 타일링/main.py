import sys
input = sys.stdin.readline

def main():
    # your code here
    n = int(input().strip())
    magic = 10_007
    if n < 3:
        answer = n
    else:
        answer = 0
        prev_prev_answer = 1
        prev_answer = 2
        for i in range(n-2):
            answer = prev_answer + prev_prev_answer
            answer %= magic
            prev_prev_answer = prev_answer
            prev_answer = answer
    print(answer)

if __name__ == "__main__":
    main()