import sys
input = sys.stdin.readline

def main():
    l, p = map(int, input().strip().split())
    attend_true = l*p
    answer = []
    newses = map(int, input().strip().split())
    for news in newses:
        answer.append(str(news - attend_true))
    print(" ".join(answer))

if __name__ == "__main__":
    main()