import sys
import heapq
input = sys.stdin.readline

def main():
    votes, answer = [], 0
    for _ in range(int(input())):
        votes.append(int(input()))
    mine, h = votes[0], []
    for vote in votes[1:]:
        heapq.heappush(h, -vote)

    answer = 0
    if h:
        while True:
            competitor = -heapq.heappop(h)
            if mine > competitor:
                break
            competitor -= 1
            mine += 1
            answer += 1
            heapq.heappush(h, -competitor)
    print(answer)

if __name__ == "__main__":
    main()