from sys import stdin
input = stdin.readline

def main():
    words = set()
    for _ in range(int(input())):
        words.add(input().rstrip())
    [print(i) for i in sorted(words, key=lambda x: (len(x), x))]

if __name__ == "__main__":
    main()