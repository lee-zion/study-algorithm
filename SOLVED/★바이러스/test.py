import unittest
from collections import defaultdict, deque


def read_file(filename):
    file = open(filename, "r")
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret


def main(input):
    n_com, n_conn = int(input[0]), int(input[1])
    visited = [0] * n_com
    graph = defaultdict(list)
    for i in range(n_conn):
        depart, dest = map(int, input[2 + i].split(" "))
        graph[depart - 1].append(dest - 1)
        graph[dest - 1].append(depart - 1)

    answer = 0
    def bfs(curr, graph, visited):
        nonlocal answer
        q = deque([curr])
        visited[curr] = 1
        while q:
            v = q.popleft()
            for adj in graph[v]:
                if not visited[adj]:
                    q.append(adj)
                    answer += 1
                    visited[adj] = 1
    bfs(0, graph, visited)
    print(answer)
    return [str(answer)]


class TestCases(unittest.TestCase):
    def test_input_txt(self):
        input = read_file("바이러스/input.txt")
        answer = read_file("바이러스/output.txt")
        self.assertEqual(main(input), answer)


if __name__ == "__main__":
    unittest.main()
