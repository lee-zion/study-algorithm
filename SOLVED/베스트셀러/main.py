import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    n = int(input())
    sell = defaultdict(int)
    for i in range(n):
        title = input().rstrip()
        sell[title] += 1
    answer = sorted(sorted(sell.items()), key=lambda x: x[1], reverse=True)
    print(answer[0][0])

if __name__ == "__main__":
    main()