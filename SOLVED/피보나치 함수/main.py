import sys

def main():
    n_test = int(sys.stdin.readline())
    n_case = []
    
    for i in range(n_test):
        n_case.append(int(sys.stdin.readline()))
    
    def fib(stack, curr):
        now = stack[curr]
        stack[curr] = 0
        stack[curr - 1] += now
        stack[curr - 2] += now

    for case in n_case:
        stack = [0]*(case + 1) if case > 0 else [0]*2
        curr = case
        stack[curr] = 1
        while curr > 1:
            fib(stack, curr)
            curr -= 1
        print(" ".join(map(str, stack[:2])))

if __name__ == "__main__":
    main()