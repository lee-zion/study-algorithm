import sys, math

def main():
    n = int(sys.stdin.readline())
    k = round(math.log(n, 3))
    paper = []
    for i in range(n):
        paper.append(list(map(int, sys.stdin.readline().rstrip().split())))
    counted = {0: 0, 1: 0, -1: 0}

    def cut_paper(paper, heart, step):
        nonlocal counted, n
        if heart == 0:
            counted[paper[0][0]] += 1
        else:
            for x in range(3):
                for y in range(3):
                    sx, sy = step * x, step * y
                    subpaper = [
                        row[sy : sy + step] for row in paper[sx : (sx + step)]
                    ]
                    is_all_same = True
                    for row in subpaper:
                        if not all(i == row[0] for i in row):
                            is_all_same = False
                            break
                    if is_all_same:
                        counted[subpaper[0][0]] += 1
                    else:
                        cut_paper(subpaper, heart - 1, step // 3)
    cut_paper(paper, k, n // 3)
    for key in range(-1, 2):
        print(counted[key])

if __name__ == "__main__":
    main()