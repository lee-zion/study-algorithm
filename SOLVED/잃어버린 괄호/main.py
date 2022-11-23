import sys

def main():
    eqn_minus = sys.stdin.readline().strip().split("-")
    for i in range(len(eqn_minus)):
        eqn_plus = eqn_minus[i].split("+")
        for j in range(len(eqn_plus)):
            if eqn_plus[j][0] == "0":
                ix = next((i for i, x in enumerate(eqn_plus[j]) if int(x)), None)
                eqn_plus[j] = eqn_plus[j][ix:] if ix else "0"
        eqn_minus[i] = str(sum(map(int, eqn_plus)))
    answer = eval(eqn_minus[0])
    if len(eqn_minus) > 1:
        for eqn_part in eqn_minus[1:]:
            answer -= eval(eqn_part)
    print(answer)

if __name__ == "__main__":
    main()