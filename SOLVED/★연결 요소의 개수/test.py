import unittest
from collections import defaultdict, deque

def read_file(filename):
    file = open(filename, 'r')
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret

def bfs(current, graph, visited):
    q = deque([])
    visited[current] = True
    q.append(current)
    while q:
        v = q.popleft()
        for adj in graph[v]:
            if not visited[adj]:
                visited[adj] = True
                q.append(adj)


def main(input):
    [N, M] = map(int, input[0].split(" "))
    graph = defaultdict(list)
    for i in range(M):
        [u, v] = map(int, input[1+i].split(" "))
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    for key in graph.keys():
        graph[key].sort()
    visited = [False] * N

    answer = 0
    while not all(visited):
        for i, is_visited in enumerate(visited):
            if not is_visited:
                answer += 1
                bfs(i, graph, visited)
    print(answer)
    return [str(answer)]

class TestCases(unittest.TestCase):
    def test_input_txt(self):
        input = read_file('★연결 요소의 개수/input.txt')
        answer = read_file('★연결 요소의 개수/output.txt')
        self.assertEqual(main(input), answer)


if __name__ == '__main__':
    unittest.main()