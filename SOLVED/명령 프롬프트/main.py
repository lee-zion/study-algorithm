import sys
input = sys.stdin.readline

def main():
    files = []
    for _ in range(int(input())):
        files.append(input().strip())
    answer = ""
    for i in range(len(files[0])):
        is_all_same = True
        reference = files[0][i]
        for file in files[1:]:
            if reference != file[i]:
                is_all_same = False
                break
        if is_all_same:
            answer += reference
        else:
            answer += "?"
    print(answer)

if __name__ == "__main__":
    main()