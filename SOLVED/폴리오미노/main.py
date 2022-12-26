import sys

def main():
    board = sys.stdin.readline().strip().split(".")
    is_solvable = True
    for i, piece in enumerate(board):
        if piece:
            l = len(piece)
            if l % 2 == 0:
                replacer = ""
                while True:
                    if l >= 4:
                        l -= 4
                        replacer += "A"*4
                    elif l >= 2:
                        l -= 2
                        replacer += "B"*2
                    else:
                        break
                board[i] = replacer
            else:
                is_solvable = False
                break
    print(".".join(board) if is_solvable else "-1")

if __name__ == "__main__":
    main()