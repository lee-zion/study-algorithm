import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
print = sys.stdout.write

def solve():   
    n, m = map(int, input().split())

    parent = list(range(n + 1))
    for _ in range(m):
        tp, a, b = map(int, input().split())
        
        while a != parent[a]:
            parent[a] = parent[parent[a]]
            a = parent[a]
            
        while b != parent[b]:
            parent[b] = parent[parent[b]]
            b = parent[b]

        if tp == 0:
            if a != b:
                if a > b:
                    a, b = b, a
                parent[b] = a
        else: print('YES\n') if a == b else print('NO\n')
            
if __name__ == '__main__':
    solve()