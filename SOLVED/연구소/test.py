import unittest
from traceback import print_exception
import sys
from collections import deque, Counter
from itertools import combinations

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
            X_MAX, Y_MAX = map(int, input[0].split())
            answer, graph = 0, []
            EMPTY, WALL, VIRUS = 0, 1, 2
            for i in range(X_MAX):
                graph.append(list(map(int, input[1+i].split())))
            
            
            def find_from(graph, val):
                found = []
                nonlocal X_MAX, Y_MAX
                for x in range(X_MAX):
                    for y in range(Y_MAX):
                        if graph[x][y] == val:
                            found.append((x, y))
                return found

            def spread_virus(viruses, graph):
                nonlocal EMPTY, VIRUS, X_MAX, Y_MAX
                q = deque(viruses)
                dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
                while q:
                    (vx, vy) = q.popleft()
                    for i in range(4):
                        nx, ny = vx + dx[i], vy + dy[i]
                        if nx < 0 or ny < 0 or nx >= X_MAX or ny >= Y_MAX:
                            continue
                        if graph[nx][ny] == EMPTY:
                            graph[nx][ny] = VIRUS
                            q.append((nx, ny))
            
            empties = find_from(graph, EMPTY)
            viruses = find_from(graph, VIRUS)

            answer = (0, ((-1, -1), (-1, -1), (-1, -1)))
            for walls in combinations(empties, 3):
                for x, y in walls:
                    graph[x][y] = WALL
                
                temp_graph = [row[:] for row in graph]
                spread_virus(viruses, temp_graph)
                candidate = len(find_from(temp_graph, EMPTY))
                if candidate > answer[0]:
                    answer = (candidate, walls)
                
                for x, y in walls:
                    graph[x][y] = EMPTY
            
            print(answer)

            answers.append(answer[0])
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
        for i in range(1, 3 + 1):
            inputs.append(read_file(f"연구소/input{i}.txt"))
            answers.append(int(read_file(f"연구소/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()