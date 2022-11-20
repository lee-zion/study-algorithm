import unittest
from collections import defaultdict

def read_file(filename):
    file = open(filename, 'r')
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret

def main(edges, roots):
    def is_my_parent(curr, root_new, graph):
        if root_new in graph[curr]:
            return True
        # root not in graph[curr]: find from its parent
        for adj in graph[curr]:
            is_my_parent(adj, root_new, graph)
        return False
    def am_i_root(curr, root):
        return True if curr == root else False
    
    graph = defaultdict(list)
    # graph records its child(arrival) to parent(depart)
    # for depart, arrival in edges:
    #     graph[depart].append(arrival)

    # graph records its parent to child
    for parent, child in edges:
        graph[child].append(parent)
    
    answer = [0] * len(roots)
    for ir, root in enumerate(roots):
        for key in graph:
            # am i root?
            print(key)
            # if not am_i_root(curr, root):
            #     if not is_my_parent(key, root, graph):
            #         answer[ir] += 1
    curr = 1
    root_init = 1
    print(am_i_root(curr, root_init))
    curr = 2
    print(is_my_parent(root_init, root_init, graph))
    # print(is_my_parent(curr, root_init, graph))
    return True

class TestCases(unittest.TestCase):
    def test_input_txt(self):
        edges = [[1, 3], [1, 2], [2, 4], [2, 5]]
        roots = [2, 3]
        answer = [1, 2, 0, 0]
        self.assertEqual(main(edges, roots), answer)


if __name__ == '__main__':
    unittest.main()