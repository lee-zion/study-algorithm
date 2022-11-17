import unittest
from collections import defaultdict, deque

def read_file(filename):
    file = open(filename, 'r')
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret

class Node:
    def __init__(self, item) -> None:
        self.item = item
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, item) -> None:
        self.root = None

def main(input):
    n = int(input[0])
    graph = defaultdict(list)
    for i in range(n-1):
        [x, y] = map(int, input[1+i].split(" "))
        graph[x].append(y)
        graph[y].append(x)
    visited = [0] * (n+1)
    def bfs(curr, graph, visited):
        q = deque([curr])
        visited[curr] = curr
        while q:
            v = q.popleft()
            for adj in graph[v]:
                if not visited[adj]:
                    visited[adj] = v
                    q.append(adj)
    bfs(1, graph, visited)
    answer = []
    for i in range(2, n+1):
        print(visited[i])
        answer.append(str(visited[i]))
    return answer

class TestCases(unittest.TestCase):
    def test_input_txt(self):
        input = read_file('트리의 부모 찾기/input.txt')
        answer = read_file('트리의 부모 찾기/output.txt')
        self.assertEqual(main(input), answer)


if __name__ == '__main__':
    unittest.main()