import sys
input = sys.stdin.readline

def main():
    # your code here
    n = int(input().strip())
    x_list = list(map(int, input().strip().split()))
    x_sorted = sorted(set(x_list))
    cache = {}
    for i, x in enumerate(x_sorted):
        if x not in cache:
            cache[x] = i
    for x in x_list:
        print(cache[x], end=" ")

if __name__ == "__main__":
    main()