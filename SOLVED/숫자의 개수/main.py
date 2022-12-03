import sys, collections, string

def main():
    num = 1
    for _ in range(3):
        num *= int(sys.stdin.readline())
    
    num_cnt = collections.Counter()
    for s in str(num):
        num_cnt[s] += 1
    for i in string.digits:
        print(num_cnt[i])

if __name__ == "__main__":
    main()