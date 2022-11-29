import sys

def main():
    answer = 1
    sum = 1
    n = int(sys.stdin.readline())
    while n > sum:
        sum += 6 * answer
        answer += 1
    print(answer)
    
if __name__ == "__main__":
    main()