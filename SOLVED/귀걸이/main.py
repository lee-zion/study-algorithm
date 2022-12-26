import sys
input = sys.stdin.readline

def main():
    gi = 1
    while True:
        name, logs = [-1], dict()
        n = int(input().strip())
        if n == 0:
            break
        for _ in range(n):
            name.append(input().strip())
        for _ in range(2*n - 1):
            id = input().strip().split()[0]
            logs[id] = logs[id] + 1 if id in logs else 1
        
        for key in logs.keys():
            if logs[key] == 1:
                print(f"{gi} {name[int(key)]}")
        gi += 1

if __name__ == "__main__":
    main()