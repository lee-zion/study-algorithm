import sys
from collections import deque

def main():
    s, n = 'ABCDEF', '123456'
    cmd = []
    [cmd.append(sys.stdin.readline()) for i in range(36)]
    if len(list(set(cmd))) != len(cmd):
        print("Invalid")
        return
    
    cmd.append(cmd[0])
    found = deque([(s.find(cmd[0][0]), n.find(cmd[0][1]))])
    is_valid = True
    for c in cmd[1:]:
        psi, pni = found.popleft()
        si, ni = s.find(c[0]), n.find(c[1])
        asi, ani = abs(si - psi), abs(ni - pni)
        if (asi == 2 and ani == 1) or (asi == 1 and ani == 2):
            found.append((si, ni))
        else:
            is_valid = False
            break
    print("Valid" if is_valid else "Invalid")

if __name__ == "__main__":
    main()