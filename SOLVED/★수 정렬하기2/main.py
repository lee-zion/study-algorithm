import sys

def main():
    N = sys.stdin.readline()
    arr = []
    for i in range(int(N)):
        arr.append(int(sys.stdin.readline()))
    arr.sort()
    for num in arr:
        print(num)
if __name__ == "__main__":
    main()