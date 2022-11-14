import sys
answer = 0
candidates = [5, 3]
target = int(sys.stdin.readline())
while target > 0:
    if target%candidates[0] == 0:
        answer += target // candidates[0]
        break
    else:
        target -= candidates[1]
        answer += 1
print(-1) if target < 0 else print(answer)