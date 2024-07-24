import sys
input = sys.stdin.readline

def main():
    n = int(input().strip())
    answer = 0
    if n < 110:
        answer = min(99, n)
    else:
        answer = 99
        for num in range(111, min(1000, n + 1)):
            a_prev = num % 10
            a_now = num // 10 % 10
            d = a_now - a_prev
            a_prev = a_now
            for i in range(2, len(str(num))):
                a_now = num // 10**(i) % 10
                if a_now - a_prev != d:
                    break
                answer += 1
                a_prev = a_now
    print(answer)


if __name__ == "__main__":
    main()