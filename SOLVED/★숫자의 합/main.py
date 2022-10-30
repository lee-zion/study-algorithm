import sys

def main():
    l = sys.stdin.readline()
    num = sys.stdin.readline()
    sum = 0
    for i in range(int(l)):
        sum += int(num[i])
    print(sum)
    return sum

if __name__ == "__main__":
    main()