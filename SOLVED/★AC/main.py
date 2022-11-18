import sys
from collections import deque

def main():
    n_test = int(sys.stdin.readline())
    offset = 0
    answer = []
    input = [n_test]
    for _ in range(n_test*3):
        input.append(sys.stdin.readline().strip())
    for i in range(1, n_test + 1):
        commands = input[offset + 1]
        merged = input[offset + 3].strip()[1:-1]
        arr = []
        if merged != "":
            arr = list(map(int, merged.split(",")))
        offset += 3
        q = deque(arr)
        is_reversed, is_error = False, False
        for cmd in commands:
            if cmd == "R":
                is_reversed = not is_reversed
            elif cmd == "D":
                if not q:
                    answer.append("error")
                    is_error = True
                    break
                elif is_reversed:
                    q.pop()
                else:
                    q.popleft()
        if not is_error:
            arr = list(q)
            if is_reversed:
                arr.reverse()
            ret = f'[{",".join(map(str, arr))}]'
            answer.append(str(ret))
    for i in answer:
        print(i)

if __name__ == "__main__":
    main()