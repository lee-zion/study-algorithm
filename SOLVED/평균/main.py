import sys

def main():
    n = int(sys.stdin.readline())
    scores = list(map(int, sys.stdin.readline().split()))
    M = max(scores)
    for i, score in enumerate(scores):
        scores[i] = score / M * 100.0
    print(sum(scores) / len(scores))

if __name__ == "__main__":
    main()