import sys, collections

def main():
    counter = collections.Counter()
    for s in sys.stdin.readline().rstrip().upper():
        counter[s] += 1
    item_max = counter.most_common(1)[0]
    len_max = len(list(filter(lambda x: x[1] == item_max[1], list(counter.items()))))
    print(item_max[0] if len_max == 1 else "?")

if __name__ == "__main__":
    main()