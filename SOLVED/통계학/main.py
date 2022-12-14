import sys
input = sys.stdin.readline
def main():
    n = int(input())
    cnt = {}
    mean = 0
    for _ in range(n):
        num = int(input())
        mean += num
        cnt[num] = cnt[num] + 1 if num in cnt else 1
    mean = round(mean / n)
    median, acc = -1, 0
    for i, key in enumerate(sorted(cnt.keys())):
        acc += cnt[key]
        if acc <= n // 2:
            continue
        median = key
        break
    
    val_max = max(cnt.values())
    max_nominee = []
    for i, key in enumerate(sorted(cnt.keys())):
        if cnt[key] == val_max:
            max_nominee.append(key)
    frequent = max_nominee[1] if len(max_nominee) > 1 else max_nominee[0]
    
    dist = max(cnt.keys()) - min(cnt.keys())
    
    print(mean)
    print(median)
    print(frequent)
    print(dist)

if __name__ == "__main__":
    main()