import sys
input = sys.stdin.readline

def main():
    # your code here
    s = set()
    n = int(input().strip())
    for _ in range(1, n+1):
        cmd = input().strip()
        if cmd == "all":
            s = set(i for i in range(1, 21))
        elif cmd == "empty":
            s.clear()
        else:
            cmd, x = cmd.split()
            x = int(x)
            if cmd == "add":
                s.add(x)
            elif cmd == "remove":
                s.discard(x)
            elif cmd == "check":
                if x in s:
                    print("1")
                else:
                    print("0")
            elif cmd == "toggle":
                if x in s:
                    s.discard(x)
                else:
                    s.add(x)
            else:
                print(f"Unknown command {cmd}")

if __name__ == "__main__":
    main()