import string, sys
input = sys.stdin.readline

def main():
    l = int(input())
    a = input()
    r, M, answer = 31, 1234567891, 0

    alpha = {char: value + 1 for value, char in enumerate(string.ascii_lowercase)}

    for i in range(l):
        answer += alpha[a[i]] * pow(r, i)
        answer %= M
    print(answer)

def main_with_ord():
    l = int(input())
    a = input()
    r, M, answer = 31, 1234567891, 0
    for i in range(l):
        answer += (ord(a[i]) - 96) * pow(r, i)
    print(answer % M)

if __name__ == "__main__":
    main()
    main_with_ord()