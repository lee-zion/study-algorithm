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
            v = int(input[0])

            tree = defaultdict(list)
            dist = defaultdict(list)
            for i in range(v):
                l = list(map(int, input[1+i].split()))[:-1]
                depart, l = l[0], l[1:]
                for j in range(0, len(l), 2):
                    arrival, adj_dist = l[j], l[j+1]
                    tree[depart].append(arrival)
                    dist[depart].append(adj_dist)

            graph = [[0] * (v+1) for _ in range(v+1)]
            for i in range(v):
                l = list(map(int, input[1+i].split()))[:-1]
                depart, l = l[0], l[1:]
                for j in range(0, len(l), 2):
                    arrival, adj_dist = l[j], l[j+1]
                    graph[depart][arrival] = adj_dist
            answer = -1
            answer_idx = -1
            def get_the_farthest_from(curr, dist_acc, visited):
                nonlocal dist, tree, answer, answer_idx
                """
                주어진 graph에서 가장 먼 node를 찾는 방법
                1) adj가 없을 때 까지 파고 들어감
                """
                print(f"curr: {curr} dist_acc: {dist_acc} answer: {answer} (at {answer_idx}) visited: {visited}")
                if dist_acc > answer:
                    answer = dist_acc
                    answer_idx = curr
                for i, adj in enumerate(tree[curr]):
                    if adj not in visited:
                        get_the_farthest_from(adj, dist_acc + dist[curr][i], visited + tuple([adj]))
            get_the_farthest_from(1, 0, (1,))
            print("-"*40)
            get_the_farthest_from(answer_idx, 0, (answer_idx,))

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
        for i in range(1, 1 + 1):
            inputs.append(read_file(f"트리의 지름/input{i}.txt"))
            answers.append(int(read_file(f"트리의 지름/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()