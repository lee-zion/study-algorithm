import sys


def main():
    plain, passphrase = sys.stdin.readline().rstrip("\n"), sys.stdin.readline().rstrip("\n")
    WHITESPACE = 32
    N_LOWERCASES = 26
    ORD_FROM_ONE = 97
    ORD_FROM_ZERO = 96
    answer = ""
    for i, c in enumerate(plain):
        if ord(c) == WHITESPACE:
            answer += c
        else:
            key = passphrase[i % len(passphrase)]
            offset = ord(key) - ORD_FROM_ZERO
            answer += chr(
                (ord(c) - ORD_FROM_ONE - offset) % N_LOWERCASES + ORD_FROM_ONE
            )
    print(answer)


if __name__ == "__main__":
    main()