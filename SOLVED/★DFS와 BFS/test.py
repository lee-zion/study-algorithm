from operator import is_
import unittest
from collections import defaultdict, deque

def read_file(filename):
    file = open(filename, 'r')
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret

def get_adj_matrix(N, g_raw, FROM_INDEX_ZERO = True):
    graph = None
    if FROM_INDEX_ZERO:
        graph = [[0 for _ in range(N)] for __ in range(N)]
    else:
        graph = [[0 for _ in range(N+1)] for __ in range(N+1)]
    for g in g_raw:
        [depart, dest] = map(int, g.split(" "))
        if FROM_INDEX_ZERO:
            graph[depart-1][dest-1] = 1
            graph[dest-1][depart-1] = 1
        else:
            graph[dest][depart] = 1
            graph[depart][dest] = 1
    return graph

def get_adj_list(g_raw, FROM_INDEX_ZERO = True, IS_BIDIR = True):
    graph = defaultdict(list)
    for g in g_raw:
        [depart, dest] = map(int, g.split(" "))
        if FROM_INDEX_ZERO:
            graph[depart-1].append(dest-1)
            if IS_BIDIR:
                graph[dest-1].append(depart-1)
        else:
            graph[depart].append(dest)
            if IS_BIDIR:
                graph[dest].append(depart)
    for g in graph.keys():
        graph[g].sort()
    return graph

def main(N, M, V, graph_raw):
    graph_mat = get_adj_matrix(N, graph_raw)
    graph_list = get_adj_list(graph_raw)
    # print(f"graph_mat : {graph_mat}")
    # print(f"graph_list: {graph_list}")

    def dfs(current, graph, visited, FROM_INDEX_ZERO = True):
        nonlocal answer
        visited[current] = True
        if FROM_INDEX_ZERO:
            answer.append(current+1)
        else:
            answer.append(current)

        if isinstance(graph, defaultdict):
            # graph == adj_list
            for adj in graph[current]:
                if not visited[adj]:
                    dfs(adj, graph, visited)
        elif isinstance(graph, list):
            # graph == adj_matrix
            for adj, is_connected in enumerate(graph[current]):
                if is_connected and not visited[adj]:
                    dfs(adj, graph, visited)
    
    def bfs(current, graph, visited, FROM_INDEX_ZERO = True):
        nonlocal answer
        q = deque([current])
        visited[current] = True
        if FROM_INDEX_ZERO:
            answer.append(current+1)
        else:
            answer.append(current)

        while q:
            current = q.popleft()
            if isinstance(graph, defaultdict):
                # graph == adj_list
                for adj in graph[current]:
                    if not visited[adj]:
                        q.append(adj)
                        visited[adj] = True
                        if FROM_INDEX_ZERO:
                            answer.append(adj+1)
                        else:
                            answer.append(adj)
            elif isinstance(graph, list):
                # graph == adj_matrix
                for adj, is_connected in enumerate(graph[current]):
                    if is_connected and not visited[adj]:
                        q.append(adj)
                        visited[adj] = True
                        if FROM_INDEX_ZERO:
                            answer.append(adj+1)
                        else:
                            answer.append(adj)
    
    print(f"---------- [list] ----------")
    print(f"---------- [DFS] ----------")
    answer, visited = [], [False] * N
    dfs(V-1, graph_list, visited)
    print(answer)

    print(f"---------- [BFS] ----------")

    answer, visited = [], [False] * N
    bfs(V-1, graph_list, visited)
    print(answer)

    print(f"---------- [matrix] ----------")
    # ISSUE: CASE3 is not solved in matrix only
    print(f"---------- [DFS] ----------")

    answer, visited = [], [False] * N
    dfs(V-1, graph_mat, visited)
    print(answer)
    
    print(f"---------- [BFS] ----------")
    answer, visited = [], [False] * N
    bfs(V-1, graph_mat, visited)
    print(answer)

    return True

class TestCases(unittest.TestCase):
    def test_input_txt(self):
        ex1_input = read_file('DFS와 BFS/input.txt')
        [N, M, V] = map(int, ex1_input[0].split(" "))
        graph = ex1_input[1:]
        ex1_output = read_file('DFS와 BFS/output.txt')
        main(N, M, V, graph)
        # self.assertEqual(main(N, M, V, graph), ex1_output)


if __name__ == '__main__':
    unittest.main()