import sys
from collections import deque
input = sys.stdin.readline

def main():
    answer = deque([])
    n = int(input())
    stack, curr, next = deque([]), 1, True
    for _ in range(n):
        dest = int(input())
        while dest >= curr and next:
            stack.append(curr)
            answer.append("+")
            curr += 1
        top = stack.pop()
        if top == dest:
            answer.append("-") 
        else:
            answer = deque(["NO"])
            next = False
    while answer:
        print(answer.popleft())

if __name__ == "__main__":
    main()