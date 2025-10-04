import sys
input = sys.stdin.readline

def main():
    # your code here
    n, m = map(int, input().strip().split())
    d = dict()
    for i in range(n):
        site, password = input().strip().split()
        d.update({site: password})
    
    for i in range(m):
        site = input().strip()
        print(d[site])

    

if __name__ == "__main__":
    main()