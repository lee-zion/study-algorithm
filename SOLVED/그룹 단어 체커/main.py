import sys
from collections import defaultdict
input = sys.stdin.readline
def main():
    answer = 0
    for i in range(int(input().strip())):
        basket = defaultdict(list)
        has_passed = True
        for si, s in enumerate(input().strip()):
            if s in basket:
                if si in basket[s]:
                    basket[s].append(si + 1)
                    continue
                has_passed = False
                break
            else:
                basket[s].append(si + 1)
        if has_passed:
            answer += 1
    print(answer)

if __name__ == "__main__":
    main()