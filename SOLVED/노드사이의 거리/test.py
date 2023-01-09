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

def main(inputs):
    answers = []
    try:
        for input in inputs:
            # your code here
            def bfs(depart, dest):
                nonlocal graph, n
                visited = [False] * (n+1)
                dist_init = 0
                q = deque([(depart, dist_init)])
                while q:
                    curr, dist_acc = q.popleft()
                    visited[curr] = True
                    if curr == dest:
                        return dist_acc
                    for curr_adj, curr_dist in graph[curr]:
                        if not visited[curr_adj]:
                            q.append((curr_adj, dist_acc + curr_dist))
            n, m = map(int, input[0].split())
            graph = defaultdict(list)
            for i in range(n-1):
                x, y, dist = map(int, input[1+i].split())
                graph[x].append((y, dist))
                graph[y].append((x, dist))
            for i in range(m):
                depart, dest = map(int, input[n+i].split())
                answers.append(str(bfs(depart, dest)))
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
            inputs.append(read_file(f"노드사이의 거리/input{i}.txt"))
            answers.append(read_file(f"노드사이의 거리/output{i}.txt"))
        self.assertEqual(main(inputs), answers[0])


if __name__ == '__main__':
    unittest.main()