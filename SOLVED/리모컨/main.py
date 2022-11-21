from sys import stdin
srl = stdin.readline
def main():
    begin, target, n_broken = 100, int(srl()), int(srl())
    candidates = set(range(10))
    if n_broken:
        candidates = list(candidates.symmetric_difference(set(map(int, srl().split()))))
    
    ans = 5*10**5 + 1
    def dfs(c):
        nonlocal ans, target, candidates
        for btn in candidates:
            c += str(btn)
            # 숫자 차이만큼 +-버튼입력횟수 + 숫자 입력에 필요한 버튼 입력횟수
            ans = min(ans, abs(int(c) - target) + len(c))
            if len(str(c)) < 6:
                dfs(c)
                c = c[:-1]
            else:
                c = c[:-1]
    dfs("")
    print(min(ans, abs(target - begin)))

if __name__ == "__main__":
    main()