import sys
input = sys.stdin.readline
from collections import defaultdict

def main():
    v = int(input())
    tree = defaultdict(list)
    dist = defaultdict(list)
    for i in range(v):
        l = list(map(int, input().strip().split()))[:-1]
        depart, l = l[0], l[1:]
        for j in range(0, len(l), 2):
            arrival, adj_dist = l[j], l[j+1]
            tree[depart].append(arrival)
            dist[depart].append(adj_dist)

    answer, idx = -1, -1
    def get_the_farthest_from(curr, dist_acc, visited):
        nonlocal dist, tree, answer, idx
        if dist_acc > answer:
            answer = dist_acc
            idx = curr
        for i, adj in enumerate(tree[curr]):
            if adj not in visited:
                get_the_farthest_from(adj, dist_acc + dist[curr][i], visited + tuple([adj]))
    get_the_farthest_from(1, 0, (1,))
    get_the_farthest_from(idx, 0, (idx,))
    print(answer)

if __name__ == "__main__":
    main()