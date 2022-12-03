import sys

def main():
    print(sum([int(n)*pow(-1,i) for i, n in enumerate(sys.stdin.readline().rstrip().split())]))

if __name__ == "__main__":
    main()