import sys

def main():
    def bin_flip(str):
        ret = ""
        for s in str:
            ret += "1" if s == "0" else "0"
        return ret
    
    def find_nth(src, to_find, n):
        begin = src.find(to_find)
        while begin >= 0 and n > 1:
            begin = src.find(to_find, begin + len(to_find))
            n -= 1
        return begin

    bottle, k = map(int, sys.stdin.readline().split())
    bottle_bin = bin(bottle)[2:]

    if bottle_bin.count("1") <= k:
        print("0")
    else:
        ik = find_nth(bottle_bin, "1", k) + 1
        ilast = bottle_bin.rfind("1")
        x = bin_flip(bottle_bin[ik:ilast]) + bottle_bin[ilast:]
        print(int(x, 2))

if __name__ == "__main__":
    main()