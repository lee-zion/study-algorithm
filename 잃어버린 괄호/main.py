import sys

def main():
    eqn = sys.stdin.readline().strip().split("-")
    for i in range(len(eqn)):
        if eqn[i][0] == "0":
            ix = next((i for i, x in enumerate(eqn[i]) if int(x)), None)
            eqn[i] = eqn[i][ix:] if ix else "0"
    answer = eval(eqn[0])
    if len(eqn) > 1:
        for eqn_part in eqn[1:]:
            eqn_plus = eqn_part.split("+")
            if len(eqn_plus) > 1:
                for i in range(len(eqn_plus)):
                    if eqn_plus[i][0] == "0":
                        ix = next((i for i, x in enumerate(eqn_plus[i]) if int(x)), None)
                        eqn_plus[i] = eqn_plus[i][ix:] if ix else "0"
                    answer -= eval(eqn_plus[i])
            else:
                answer -= eval(eqn_part)
    print(answer)

if __name__ == "__main__":
    main()