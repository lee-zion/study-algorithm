import sys

def main():
    n_pots, n_friend = map(int, sys.stdin.readline().split())
    pots = []
    [pots.append(int(sys.stdin.readline())) for _ in range(n_pots)]
    bracket = [0, max(pots)]
    while bracket[1] - bracket[0] > 1e-02:
        mid = sum(bracket) / 2
        filled = 0
        for pot in pots:
            filled += pot // mid
        if filled < n_friend:
            bracket[1] = mid
        else:
            bracket[0] = mid
    print(int(bracket[1]))

if __name__ == "__main__":
    main()