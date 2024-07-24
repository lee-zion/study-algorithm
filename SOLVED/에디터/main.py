import sys
input = sys.stdin.readline
from collections import deque

def main():
    str_init = input().strip()
    num_cmd = int(input())
    cmds = []
    for _ in range(num_cmd):
        cmds.append(input().strip())
    left, right = deque([]), deque([])
    for c in str_init:
        left.append(c)
    
    for cmd in cmds:
        if cmd[0] == "P":
            left.append(cmd[-1])
        elif cmd[0] == "B" and left:
            left.pop()
        elif cmd[0] == "L" and left:
            right.appendleft(left.pop())
        elif cmd[0] == "D" and right:
            left.append(right.popleft())
    print("".join(left) + "".join(right))

if __name__ == "__main__":
    main()