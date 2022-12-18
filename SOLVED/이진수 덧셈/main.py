import sys
input = sys.stdin.readline

def main():
    T = int(input())
    for i in range(T):
        l, r = map(lambda x: int(x, 2), input().rstrip().split())
        print(bin(l + r)[2:])

if __name__ == "__main__":
    main()