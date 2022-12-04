import unittest
from traceback import print_exception
import sys


def read_file(filename):
    file = open(filename, "r")
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret


def main(inputs):
    answers = []
    try:
        GRAPH_INIT = 10**4 + 1
        for input in inputs:
            # your code here
            T = int(input[0])
            offset = 0
            for i in range(T):
                # n: number of node, [1, 500]
                # m: number of road, [1, 2500]
                # w: number of wormhole, [1, 200]
                n, m, w = map(int, input[1 + i + offset].split())
                
                roads = []
                for i_road in range(1, m + 1):
                    # s, e, t
                    # s,e: node s and e are connected to each other
                    # t: time needed, t \in [0, 10**4]
                    roads.append(
                        list(map(int, input[1 + i + offset + i_road].split()))
                    )
                holes = []
                for i_hole in range(1, w + 1):
                    # wormhole: one-way road
                    # s, e, t
                    # s: starting
                    # e: ending
                    # t: time decreased, t \in [0, 10**4]
                    holes.append(
                        list(
                            map(int, input[1 + i + offset + m + i_hole].split())
                        )
                    )
                graph = [ [GRAPH_INIT] * (n) for _ in range(n)]
                for s, e, t in roads:
                    graph[s-1][e-1] = min(graph[s-1][e-1], t)
                    graph[e-1][s-1] = min(graph[e-1][s-1], t)
                for s, e, t in holes:
                    graph[s-1][e-1] = -t
                
                for i in range(n):
                    for j in range(n):
                        if graph[i][j] == GRAPH_INIT:
                            graph[i][j] = 0
                
                # 완전탐색?
                def dfs(time, curr, graph, visited):
                    nonlocal answer, begin
                    # answer = min(answer, time)
                    # 나 자신에게 돌아오는 path 전부 찾기
                    if curr == begin:
                        answer = min(answer, time)
                    else:
                        for col, adj in enumerate(graph[curr]):
                            # print(f"col: {col}   adj: {adj}   curr: {curr}")
                            # print(f"col: {type(col)}   adj: {type(adj)}   curr: {type(curr)}")
                            if not visited[col] and adj != 0:
                                visited[col] = True
                                dfs(time + adj, col, graph, visited)
                                visited[col] = False
                answer = 0
                for begin in range(n):
                    answer = GRAPH_INIT
                    visited = [False] * (n+1)
                    for row, adj in enumerate(graph[begin]):
                        dfs(adj, row, graph, visited)
                        if answer < 0:
                            answer = "YES"
                            break
                    if answer != "YES":
                        answer = "NO"

                offset = offset + m + w
                answers.append(answer)
        return answers
    except Exception:
        print(
            f"==========================================================================="
        )
        print(f"Failed in the case below")
        print(f"input: {input}")
        exc_info = sys.exc_info()
        print_exception(*exc_info)
        print(
            f"==========================================================================="
        )
        del exc_info


class TestCases(unittest.TestCase):
    def test_input_txt(self):
        inputs, answers = [], []
        for i in range(3, 3 + 1):
            inputs.append(read_file(f"웜홀/input{i}.txt"))
            answers.append(read_file(f"웜홀/output{i}.txt"))
        self.assertEqual(main(inputs), answers[0])


if __name__ == "__main__":
    unittest.main()
