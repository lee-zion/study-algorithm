import unittest

def read_file(filename):
    file = open(filename, 'r')
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret

def main(input):
    [n_pokemon, n_problem] = list(map(int, input[0].split(" ")))
    n_pokemon += 1

    pokedex = [False]
    for i in range(n_pokemon):
        pokedex.append(input[1+i])
    
    answer = []
    for problem in range(n_problem, 0, -1):
        read = input[-problem]
        if read.isdigit():
            read = int(read)
            print(pokedex[read])
            answer.append(pokedex[read])
        else:
            print(pokedex.index(read))
            answer.append(str(pokedex.index(read)))
    return answer

class TestCases(unittest.TestCase):
    def test_input_txt(self):
        input = read_file('나는야 포켓몬 마스터 이다솜/input.txt')
        answer = read_file('나는야 포켓몬 마스터 이다솜/output.txt')
        self.assertEqual(main(input), answer)


if __name__ == '__main__':
    unittest.main()