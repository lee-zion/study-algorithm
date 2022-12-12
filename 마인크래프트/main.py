import sys

def main():
    TIME_INIT, BLOCK_INIT = -1, 257
    X_MAX, Y_MAX, block = map(int, sys.stdin.readline().rstrip().split())
    lands = []
    h_min, h_max = 0, 0
    for _ in range(X_MAX):
        land = list(map(int, sys.stdin.readline().rstrip().split()))
        h_min, h_max = min(h_min, min(land)), max(h_max, max(land))
        lands.append(land)
    
    diff = [[0] * Y_MAX for _ in range(X_MAX)]
    diff_cnt = {}
    for x in range(X_MAX):
        for y in range(Y_MAX):
            subtract = lands[x][y] - h_min
            diff_cnt[subtract] = diff_cnt[subtract] + 1 if subtract in diff_cnt else 1
            diff[x][y] = subtract
    
    answer = (TIME_INIT, BLOCK_INIT)
    for target in range(0, h_max - h_min + 1):
        cost, block_needed = 0, 0
        for key in diff_cnt.keys():
            subtract = key - target
            if subtract > 0:
                cost += diff_cnt[key] * 2 * subtract
            elif subtract < 0:
                cost += diff_cnt[key]
                block_needed += diff_cnt[key]
        if block < block_needed:
            break
        if answer[0] != TIME_INIT:
            if cost <= answer[0]:
                answer = (cost, h_min + target)
        else:
            answer = (cost, h_min + target)
    print(f"{answer[0]} {answer[1]}")
if __name__ == "__main__":
    main()