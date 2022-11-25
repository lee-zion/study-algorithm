import sys

def main():
    n = int(sys.stdin.readline())
    meetings = [list(map(int, sys.stdin.readline().split())) for j in range(n)]
    answer = 1
    meetings = sorted(meetings, key = lambda x: (x[1], x[0]))
    begin_now, end_now = meetings[0]
    for begin_new, end_new in meetings[1:]:
        if begin_new >= end_now:
            end_now = end_new
            answer += 1
    print(answer)

if __name__ == "__main__":
    main()