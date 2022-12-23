import sys
input = sys.stdin.readline

def main():
    BLOCK_MAX = 256
    blocks = [0]*(BLOCK_MAX + 1)
    X_MAX, Y_MAX, block = map(int, input().split())
    for i in range(X_MAX):
        for e in map(int, input().split()):
            blocks[e] += 1
    block_sum = sum(i*blocks[i] for i in range(BLOCK_MAX + 1))
    answer = (block_sum * 2, 0)
    subtract_one_for_all = X_MAX * Y_MAX
    block_needed = 0
    acc = blocks[0]
    for i in range(1, BLOCK_MAX + 1):
        block_needed += acc
        block_sum -= subtract_one_for_all - acc
        acc += blocks[i]
        if block_needed > block_sum + block:
            break
        else:
            answer = min(answer, (block_needed + block_sum * 2, -i))
    print(f"{answer[0]} {-answer[1]}")
if __name__ == "__main__":
    main()