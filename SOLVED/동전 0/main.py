import sys
input = sys.stdin.readline

def main():
    # your code here
    n, k = map(int, input().strip().split())
    coins = []
    for i in range(n):
        coins.append(int(input().strip()))
    answer = 0
    while k != 0:
        coin = coins.pop()
        if k < coin:
            continue
        q, r = divmod(k, coin)
        answer += q
        k = r
    print(answer)

if __name__ == "__main__":
    main()