import sys
input = sys.stdin.readline

def main():
    for i in range(int(input()), 0, -1):
        print("*"*i)

if __name__ == "__main__":
    main()