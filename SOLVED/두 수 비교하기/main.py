import sys

def main():
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if a > b:
        print(">")
    elif a < b:
        print("<")
    else:
        print("==")

if __name__ == "__main__":
    main()