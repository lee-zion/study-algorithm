import sys
from collections import deque

def main():
    answer = ""
    operators = deque([])
    given = sys.stdin.readline()
    for s in given:
        if s in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            answer += s
        else:
            if s == "(":
                operators.append(s)
            elif s == ")":
                while operators and operators[-1] != "(":
                    top = operators.pop()
                    answer += top
                operators.pop()
            elif s in ["*", "/"]:
                while operators and operators[-1] in ["*", "/"]:
                    top = operators.pop()
                    answer += top
                operators.append(s)
            elif s in ["+", "-"]:
                while operators and operators[-1] != "(":
                    top = operators.pop()
                    answer += top
                operators.append(s)
    while operators:
        top = operators.pop()
        answer += top
    print(answer)

if __name__ == "__main__":
    main()