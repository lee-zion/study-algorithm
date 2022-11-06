import sys

def main():
    [n_pokemon, n_problem] = list(map(int, sys.stdin.readline().split(" ")))
    n_pokemon += 1

    pokedex_dict = {}
    pokedex_list = [False]

    for i in range(n_pokemon - 1):
        pokemon_name = sys.stdin.readline().strip()
        pokedex_dict[pokemon_name] = i + 1
        pokedex_list.append(pokemon_name)
    
    questions = []
    for i in range(n_problem):
        questions.append(sys.stdin.readline().strip())
    
    for problem in range(n_problem):
        read = questions[problem]
        if read.isdigit():
            print(pokedex_list[int(read)])
        else:
            print(pokedex_dict[read]) 

if __name__ == "__main__":
    main()