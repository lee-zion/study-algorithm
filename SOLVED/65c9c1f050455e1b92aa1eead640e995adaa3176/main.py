from sys import stdin
from math import log2
input = stdin.readline

def main():
    n = int(input())
    k = int(log2(n / 3))
    S = pow(3, k)
    size = 3*pow(2, k+1) - 1
    tree = [[" "] * size for _ in range(n)]

    def print_star(depth, x, y):
        nonlocal tree
        if depth == 0:
            tree[x][y+2] = "*"
            tree[x+1][y+1] = "*"
            tree[x+1][y+3] = "*"
            for dy in range(5):
                tree[x+2][y+dy] = "*"
        else:
            d = 3 * pow(2, depth - 1)
            dx = [d, 0, d]
            dy = [0, d, d*2]
            for i in range(3):
                print_star(depth - 1, x + dx[i], y + dy[i])
    
    print_star(k, 0, 0)
    for i in range(n):
        print("".join(tree[i]))

if __name__ == "__main__":
    main()