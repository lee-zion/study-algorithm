import sys

def main():
    print(bin(int(sys.stdin.readline())).count("1"))

if __name__ == "__main__":
    main()