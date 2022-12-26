import sys

def main():
    def find_parent(parent, x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]
    
    def union_parent(parent, acquaints, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)

        if a in acquaints and b in acquaints:
            return
        if a in acquaints:
            parent[b] = a
            return
        if b in acquaints:
            parent[a] = b
            return
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    
    n_people, n_party = map(int, sys.stdin.readline().split())
    acquaints = list(map(int, sys.stdin.readline().split()))[1:]
    
    parents = [0] * (n_people + 1)
    for i in range(1, n_people + 1):
        parents[i] = i
    
    parties = []
    for _ in range(n_party):
        party = list(map(int, sys.stdin.readline().split()))
        n_party = party[0]
        party = party[1:]
        for attender in range(n_party - 1):
            union_parent(parents, acquaints, party[attender], party[attender + 1])
        parties.append(party)
    answer = 0
    for party in parties:
        for attender in party:
            ret = find_parent(parents, attender)
            if ret in acquaints:
                break
        else:
            answer += 1
    print(answer)

if __name__ == "__main__":
    main()