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
            
            
            def find_empty(graph):
                empties = []
                nonlocal X_MAX, Y_MAX, EMPTY
                for x in range(X_MAX):
                    for y in range(Y_MAX):
                        if graph[x][y] == EMPTY:
                            empties.append((x, y))
                return empties

            def column(matrix, i):
                return [row[i] for row in matrix]

            def find_virus(graph):
                viruses = []
                nonlocal X_MAX, Y_MAX, VIRUS
                for x in range(X_MAX):
                    for y in range(Y_MAX):
                        if graph[x][y] == VIRUS:
                            viruses.append((x, y))
                return viruses
            
            def spread_virus(viruses, graph):
                nonlocal EMPTY, VIRUS, X_MAX, Y_MAX
                q = deque(viruses)
                dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
                visited = [[False] * X_MAX for _ in range(Y_MAX)]
                while q:
                    (vx, vy) = q.popleft()
                    nx, ny = vx + dx[i], vy + dy[i]
                    if vx < 0 or vy < 0 or vx >= X_MAX or vy >= Y_MAX:
                        continue
                    if graph[nx][ny] == EMPTY and not visited[nx][ny]:
                        visited[nx][ny] = True
                        graph[nx][ny] = VIRUS
                        q.append((nx, ny))
            
            def get_empty_after_walled(empties, empty2wall):
                remained = Counter()
                f_empties = []
                for e in empties:
                    if e in remained:
                        remained[e] -= 1
                    else:
                        f_empties.append(e)
                return f_empties
            
            def get_safeties(empties, walled, graph):
                nonlocal EMPTY
                COUNTED = -2
                cnt = 0
                dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
                f_empties = get_empty_after_walled(empties, walled)
                q = deque([f_empties])
                visited = [[False] * X_MAX for _ in range(Y_MAX)]
                while q:
                    v = q.popleft()
                for x in range(X_MAX):
                    for y in range(Y_MAX):
                        for i in range(4):
                            vx, vy = x + dx[i], y + dy[i]
                            if vx < 0 or vy < 0 or vx >= X_MAX or vy >= Y_MAX:
                                continue
                        if graph[x][y] == EMPTY:
                            cnt += 1
                return cnt
            def solve(viruses, empties, graph):
                nonlocal answer, WALL, EMPTY
                dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
                for empty2wall in combinations(empties, 3):
                    for x, y in empty2wall:
                        graph[x][y] = WALL
                    spread_virus(viruses, graph)
                    get_safeties(graph, empty2wall, graph)
                    for x, y in empty2wall:
                        graph[x][y] = EMPTY
            empties = find_empty(graph)
            viruses = find_virus(graph)
            answer = bfs(empties, graph)

            answers.append(answer)
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