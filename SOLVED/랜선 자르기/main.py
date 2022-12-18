import sys

def main():
    n, target = map(int, sys.stdin.readline().strip().split())
    cables = []
    [cables.append(int(sys.stdin.readline())) for _ in range(n)]
    bracket = [0, max(cables)]
    while bracket[1] - bracket[0] > 1e-04:
        mid = sum(bracket) / 2
        n_made = 0
        for cable in cables:
            n_made += cable // mid
        if n_made < target:
            bracket[1] = mid
        else:
            bracket[0] = mid
    print(int(bracket[1]))

if __name__ == "__main__":
    main()