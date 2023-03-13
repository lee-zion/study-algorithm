import sys
input = sys.stdin.readline

class Tree():
    def __init__(self, n) -> None:
        self.root = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]

    def find(self, x):
        rx = self.root[x]
        if rx == x:
            return x
        else:
            self.root[x] = self.find(rx)
            return self.root[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if self.rank[ry] > self.rank[rx]:
            rx, ry = ry, rx
        self.root[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1

def main():
    n, m = map(int, input().strip().split())
    tree = Tree(n+1)
    for _ in range(m):
        op, a, b = map(int, input().strip().split())
        if op:
            print("YES" if tree.find(a) == tree.find(b) else "NO")
        else:
            tree.union(a, b)

if __name__ == "__main__":
    main()