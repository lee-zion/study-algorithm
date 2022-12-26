import sys

def main():
    given = sys.stdin.readline().strip()
    answer = []
    l = len(given)
    for i in range(l-2):
        for j in range(i + 1, l-1):
            s1, s2, s3 = given[:i+1], given[i+1:j+1], given[j+1:]
            answer.append(s1[::-1] + s2[::-1] + s3[::-1])
    print(sorted(answer)[0])

if __name__ == "__main__":
    main()