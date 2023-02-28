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
            def get_max_dou_with_key(graph):
                dou = (0, -1)
                """
                dou = 0
                q = deque([begin])
                while q:
                    curr = q.popleft()
                    for child in graph[curr]:
                        if not visited[child]:
                            q.append(child)
                            dou += 1
                """
                dou, dou_key = 0, -1
                visited = defaultdict(set)
                keys = graph.keys()

                """
                Error of today
                RuntimeError: dictionary changed size during iteration
                
                Code block)
                for key in graph.keys():
                    q = deque([key])
                    while q:
                        curr = q.popleft()
                        for adj in graph[curr]:
                            if not graph[adj]:
                                continue
                            q.append(adj)

                AS-IS)
                `if not graph[adj]` create a new key adj to graph, which changes graph.keys() list at higher-level for loop

                TO-BE)
                ...
                if adj in graph.keys():
                    ...

                or
                
                (if graph can have a lot of key)
                keys = graph.keys()
                for key in keys:
                    ...
                    if adj not in keys:
                        ...
                """
                for key in keys:
                    temp = 0
                    q = deque([key])
                    visited[key].add(key)
                    while q:
                        curr = q.popleft()
                        temp += len(graph[curr])
                        for adj in graph[curr]:
                            if adj in visited[key]:
                                continue
                            if adj not in keys:
                                continue
                            q.append(adj)
                            visited[key].add(adj)
                    if temp > dou:
                        dou = temp
                        dou_key = key
                return (dou_key, dou)

            def remove_i_from_tree(graph, i):
                after = defaultdict(list)
                for key in graph.keys():
                    if key == i:
                        continue
                    for adj in graph[key]:
                        if adj == i:
                            continue
                        after[key].append(adj)
                return after
            def create_domino_graph(graph, pl, hl, n):
                """
                i    j
                n -> check nothing
                n-1 -> check n-th domino is reachable or not
                n-2 -> check (n-1)-th, n-th dominos are reachable or not
                ...
                1 -> check 1st, 2nd, ..., n-th dominos are reachable or not
                """
                for i in range(n-1, -1, -1):
                    pi, hi = p_list[i], h_list[i]
                    for j in range(i + 1, n):
                        pj, hj = p_list[j], h_list[j]
                        if pi + hi < pj:
                            break
                        graph[i].append(j)
            
            # parse input
            p_list = list(map(int, input[0].split()))
            h_list = list(map(int, input[1].split()))
            m = int(input[2])
            n = len(p_list)
            
            graph = defaultdict(list)
            create_domino_graph(graph, p_list, h_list, n)

            for _ in range(m):
                dou_key, dou_val = get_max_dou_with_key(graph)
                graph = remove_i_from_tree(graph, dou_key)
            _, answer = get_max_dou_with_key(graph)
            if answer == -1:
                answer = 0
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
        for i in range(1, 6 + 1):
            inputs.append(read_file(f"software-maestro/3/input{i}.txt"))
            answers.append(int(read_file(f"software-maestro/3/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()