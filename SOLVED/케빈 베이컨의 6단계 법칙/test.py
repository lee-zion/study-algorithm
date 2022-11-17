import unittest
from collections import deque, defaultdict

def read_file(filename):
    file = open(filename, 'r')
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret

def main(input):
    n_user, n_given = map(int, input[0].split())
    n_graph = n_user + 1
    # graph = [[0 for _ in range(n_graph)] for _ in range(n_graph)]
    graph = defaultdict(list)

    for i in range(n_given):
        a, b = list(map(int, input[i + 1].split()))
        graph[a].append(b)
        graph[b].append(a)
        # graph[a][b] = 1
        # graph[b][a] = 1
    
    def bfs(curr, visited):
        q = deque([curr])
        visited[curr] = 1
        while q:
            x = q.popleft()
            for y in graph[x]:
                if not visited[y]:
                    visited[y] = visited[x] + 1
                    q.append(y)
    answer = []
    for row in range(1, n_graph):
        visited = [0] * n_graph
        bfs(row, visited)
        answer.append(sum(visited))
    
    return [str(answer.index(min(answer)) + 1)]

class TestCases(unittest.TestCase):
    def test_input_txt(self):
        input = read_file('케빈 베이컨의 6단계 법칙/input.txt')
        answer = read_file('케빈 베이컨의 6단계 법칙/output.txt')
        self.assertEqual(main(input), answer)

if __name__ == '__main__':
    unittest.main()