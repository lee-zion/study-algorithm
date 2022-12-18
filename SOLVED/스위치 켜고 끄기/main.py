import sys
input = sys.stdin.readline

def flip(l, pos):
    l[pos] = "1" if l[pos] == "0" else "0"

def main():
    MALE = 1
    n_switch = int(input())
    switch = [""] + input().strip().split()
    n_student = int(input())
    for _ in range(n_student):
        sex, given = map(int, input().strip().split())
        if sex == MALE:
            i = 1
            while True:
                flip(switch, given * i)
                i += 1
                if given * i > n_switch:
                    break
        else:
            flip(switch, given)
            offset = 1
            while True:
                if given + offset > n_switch or given - offset <= 0:
                    break
                if switch[given + offset] == switch[given - offset]:
                    flip(switch, given + offset)
                    flip(switch, given - offset)
                    offset += 1
                else:
                    break
    switch = switch[1:]
    for i in range(1 + n_switch // 20):
        print(' '.join(switch[20*i:20*(i+1)]))

if __name__ == "__main__":
    main()