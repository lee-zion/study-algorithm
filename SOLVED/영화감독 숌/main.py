import sys

def main():
    target = int(sys.stdin.readline())
    answer = 666
    cnt = 1
    while True:
        if target == cnt:
            break
        answer += 1
        if "666" in str(answer):
            cnt += 1
    print(answer)

if __name__ == "__main__":
    main()