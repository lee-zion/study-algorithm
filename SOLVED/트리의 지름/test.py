import unittest
from traceback import print_exception
import sys
from collections import defaultdict, deque

def read_file(filename):
    file = open(filename, 'r')
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret

class Node(object):
    def __init__(self, item) -> None:
        self.item = item
        self.left = self.right = None

class BinaryTree(object):
    def __init__(self) -> None:
        self.root = None

def main(inputs):
    answers = []
    try:
        for input in inputs:
            # your code here
            n = int(input[0])
            graph = defaultdict(list)
            for i in range(n-1):
                parent, child, weight = list(map(int, input[1+i].split()))
                graph[parent].append((child, weight))
                graph[child].append((parent, weight))

            # DFS
            # def dfs_get_most_far_from(curr, acc):
            #     nonlocal graph, dist, i_dist, visited
            #     if acc > dist:
            #         dist = acc
            #         i_dist = curr
            #     visited[curr] = True
            #     for v_adj, w_adj in graph[curr]:
            #         if not visited[v_adj]:
            #             get_most_far_from(v_adj, acc + w_adj)
            # curr = 1
            # dist, i_dist = 0, -1
            # visited = [False] * (n+1)
            # dfs_get_most_far_from(curr, 0)
            # dist = 0
            # visited = [False] * (n+1)
            # dfs_get_most_far_from(i_dist, 0)
            # answers.append(dist)

            # BFS
            def bfs_get_most_far_from(begin):
                nonlocal graph, dist, i_dist, visited
                q = deque([(begin, 0)])
                while q:
                    curr, acc = q.popleft()
                    visited[curr] = True
                    if acc > dist:
                        dist = acc
                        i_dist = curr
                    for next, w_next in graph[curr]:
                        if not visited[next]:
                            q.append((next, acc + w_next))
            curr = 1
            dist, i_dist = 0, -1
            visited = [False] * (n+1)
            bfs_get_most_far_from(curr)
            dist = 0
            visited = [False] * (n+1)
            bfs_get_most_far_from(i_dist)
            answers.append(dist)

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
            inputs.append(read_file(f"트리의 지름/input{i}.txt"))
            answers.append(int(read_file(f"트리의 지름/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()