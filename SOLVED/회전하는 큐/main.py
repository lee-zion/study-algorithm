import sys
input = sys.stdin.readline
from collections import deque

def main():
    n, m = map(int, input().strip().split())
    q = deque([i for i in range(1, n+1)])
    targets = list(map(int, input().strip().split()))

    def get_dist(target, _list):
        forward = _list.index(target)
        backward = len(_list) - forward
        distance = min(forward, backward)
        direction = 1 if distance == forward else -1
        return (distance, direction)
    answer = 0
    for target in targets:
        dist, dir = get_dist(target, q)
        for _ in range(dist):
            q.append(q.popleft()) if dir == 1 else q.appendleft(q.pop())
            answer += 1
        q.popleft()
    print(answer)

if __name__ == "__main__":
    main()