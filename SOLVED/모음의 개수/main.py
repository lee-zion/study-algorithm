import sys
input = sys.stdin.readline

def main():
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    while True:
        sentence = input().strip()
        if sentence == "#":
            break
        n_vowel = 0
        for s in sentence:
            if s in vowels:
                n_vowel += 1
        print(n_vowel)
        offset += 1

if __name__ == "__main__":
    main()