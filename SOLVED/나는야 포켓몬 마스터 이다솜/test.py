import unittest


def read_file(filename):
    file = open(filename, "r")
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret


def main(input):
    [n_pokemon, n_problem] = list(map(int, input[0].split(" ")))
    n_pokemon += 1

    pokedex_dict = {} # key: pokemon name, value: index
    pokedex_list = [False] # key: index, value: pokemon name

    for i in range(n_pokemon - 1):
        pokemon_name = input[1+i]
        pokedex_dict[pokemon_name] = i + 1
        pokedex_list.append(pokemon_name)

    answer = []
    for problem in range(n_problem, 0, -1):
        read = input[-problem]
        if read.isdigit():
            read = int(read)
            print(pokedex_list[read])
            answer.append(pokedex_list[read])
        else:
            print(pokedex_dict[read])
            answer.append(str(pokedex_dict[read]))
    return answer


class TestCases(unittest.TestCase):
    def test_input_txt(self):
        input = read_file("나는야 포켓몬 마스터 이다솜/input.txt")
        answer = read_file("나는야 포켓몬 마스터 이다솜/output.txt")
        self.assertEqual(main(input), answer)


if __name__ == "__main__":
    unittest.main()
