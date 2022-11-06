import sys

def main():
    [n_pokemon, n_problem] = list(map(int, sys.stdin.readline().split(" ")))
    n_pokemon += 1

    pokedex = [False]
    for i in range(n_pokemon-1):
        pokedex.append(sys.stdin.readline().strip())
    
    questions = []
    for i in range(n_problem):
        questions.append(sys.stdin.readline().strip())
    for problem in range(n_problem):
        read = questions[problem]
        if read.isdigit():
            read = int(read)
            print(pokedex[read])
        else:
            print(pokedex.index(read)) 

if __name__ == "__main__":
    main()