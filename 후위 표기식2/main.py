import sys
import string
from collections import deque
input = sys.stdin.readline

def main():
    n_var = int(input())
    equation = input().strip()
    vals = []
    for i in range(n_var):
        vals.append(int(input()))
    
    def get_alphabet_idx(c):
        return vals[string.ascii_uppercase.find(c)]
    
    q = deque([])
    for s in equation:
        if s in ["+", "-", "*", "/"]:
            a = q.pop()
            b = q.pop()
            c = eval(f"{b}{s}{a}")
            q.append(c)
        else:
            q.append(get_alphabet_idx(s))
    print("{:.2f}".format(q.pop()))

if __name__ == "__main__":
    main()