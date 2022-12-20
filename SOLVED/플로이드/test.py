import unittest
from traceback import print_exception
import sys

def read_file(filename):
    file = open(filename, 'r')
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret

def main(inputs):
    answers = []
    try:
        for input in inputs:
            # your code here
            n_cities, n_buses = map(int, [input[0], input[1]])
            n_vertex = n_cities + 1
            VAL_INF = pow(10, 10) + 1
            # graph = [[] for _ in range(n_vertex)]
            # for bus in range(n_buses):
            #     depart, dest, cost = map(int, input[2+bus].split())
            #     graph[depart].append((dest, cost))
            graph = [[VAL_INF] * (n_vertex) for _ in range(n_vertex)]
            for i in range(n_vertex):
                graph[i][i] = 0
            for bus in range(n_buses):
                depart, dest, cost = map(int, input[2+bus].split())
                graph[depart][dest] = min(graph[depart][dest], cost)
            
            def floyd(graph):
                nonlocal n_vertex, VAL_INF
                # dist = [[VAL_INF] * (n_vertex) for _ in range(n_vertex)]
                for k in range(1, n_vertex):
                    for i in range(1, n_vertex):
                        for j in range(1, n_vertex):
                            dist_curr = graph[i][k] + graph[k][j]
                            graph[i][j] = min(graph[i][j], dist_curr)
                for i in range(1, n_vertex):
                    for j in range(1, n_vertex):
                        if graph[i][j] == VAL_INF:
                            graph[i][j] = 0
                return [" ".join(map(str, i[1:])) for i in graph[1:]]
            answers = floyd(graph)
        return answers
    except Exception:
        print(f"===========================================================================")
        print(f"Failed in the case below")
        print(f"input: {input}")
        exc_info = sys.exc_info()
        print_exception(*exc_info)
        print(f"===========================================================================")
        del exc_info
class TestCases(unittest.TestCase):
    def test_input_txt(self):
        inputs, answers = [], []
        for i in range(1, 1 + 1):
            inputs.append(read_file(f"플로이드/input{i}.txt"))
            answers.append(read_file(f"플로이드/output{i}.txt"))
        self.assertEqual(main(inputs), answers[0])


if __name__ == '__main__':
    unittest.main()