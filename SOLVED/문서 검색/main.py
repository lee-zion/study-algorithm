import sys
input = sys.stdin.readline

def main():
    given: str = input().strip()
    word: str = input().strip()
    l_given, offset = len(given), len(word)
    head, answer = 0, 0
    while head < l_given:
        i = given[head:].find(word)
        if i == -1:
            break
        else:
            answer += 1
            head += i + offset
    print(answer)
if __name__ == "__main__":
    main()