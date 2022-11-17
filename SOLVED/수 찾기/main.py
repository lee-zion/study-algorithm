import sys

def main():
    n_given = int(sys.stdin.readline())
    given = set(map(int, sys.stdin.readline().split()))
    n_find = int(sys.stdin.readline())
    to_find = list(map(int, (sys.stdin.readline().split()))) if n_find > 1 else [int(sys.stdin.readline())]
    for i in to_find:
        if i in given:
            print("1")
        else:
            print("0")
if __name__ == "__main__":
    main()