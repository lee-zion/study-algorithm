import sys
input = sys.stdin.readline

def main():
    # your code here
    n, target = map(int, input().strip().split())
    trees = list(map(int, input().strip().split()))
    left, right = 0, max(trees)
    answer = right
    while left <= right:
        mid = (left + right) // 2
        cut = 0
        for tree in trees:
            cut += max(0, tree - mid)
        if cut >= target:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    print(answer)
            

if __name__ == "__main__":
    main()