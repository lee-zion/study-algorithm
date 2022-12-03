import sys

def main():
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        R, S = sys.stdin.readline().strip().split()
        answer = ""
        for i, s in enumerate(S):
            answer += S[i] * int(R)
        print(answer)

if __name__ == "__main__":
    main()