# EM Pattern = (100+1+ | 01)+
# basis vector of vega space = { 01, 100+1+ }
# -> check if string can be parsed to 01 or 100+1+
import re
import sys
N = int(sys.stdin.readline())
ci = []
for _ in range(N):
    ci.append(sys.stdin.readline().strip())
for c in ci:
    if len(c) < 2:
        print('NO')
        continue
    if re.fullmatch('(100+1+|01)+', c):
        print('YES')
    else:
        print('NO')