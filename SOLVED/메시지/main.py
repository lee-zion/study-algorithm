import sys
input = sys.stdin.readline
def main():
    answer = []
    n_group, groups = 0, []
    def nasty(writer, receiver):
        return f"{writer} was nasty about {receiver}"
    def no_nasty():
        return "Nobody was nasty"
    while True:
        group = []
        n = int(input())
        if n == 0:
            break
        for i in range(n):
            group.append(input().split())
        groups.append(group)
    
    for ig, group in enumerate(groups):
        if ig != 0:
            answer.append("")
        answer.append(f"Group {ig+1}")
        for ip, paper in enumerate(group):
            for i, comment in enumerate(paper[1:]):
                if comment == "N":
                    answer.append(nasty(group[(ip-i-1) % len(group)][0], paper[0]))
        if answer[-1] == f"Group {ig+1}":
            answer.append(no_nasty())
    [print(i) for i in answer]
if __name__ == "__main__":
    main()