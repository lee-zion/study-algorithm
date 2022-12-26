import sys
input = sys.stdin.readline

def main():
    votes, answer = [], 0
    for _ in range(int(input())):
        votes.append(int(input()))
    while True:
        M = max(votes)
        iM = votes.index(M)
        if iM == 0:
            if votes[::-1].index(M) != len(votes) - 1:
                answer += 1
            break
        q, r = divmod(M - votes[0], 2)
        diff = q + r
        votes[0] += diff
        votes[iM] -= diff
        answer += diff
    print(answer)

if __name__ == "__main__":
    main()