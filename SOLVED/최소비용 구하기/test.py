import unittest
from traceback import print_exception
import sys
from collections import deque
from heapq import heappop, heappush

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
            cities, buses = map(int, (input[0], input[1]))
            # INF = -1
            VAL_INF, KEY_INF = pow(10, 10) + 1, -1
            # graph = [[] for _ in range(cities + 1)]
            graph = [[VAL_INF]*(cities + 1) for _ in range(cities + 1)]
            
            # initialize distance table
            # if there are multiple path, set to min value
            for bus in range(buses):
                depart, dest, cost = map(int, input[2+bus].split())
                graph[depart][dest] = min(graph[depart][dest], cost)
            
            # set departure/destination node
            depart, dest = map(int,input[2 + buses].split())
            visited = [False] * (cities + 1)

            def dijkstra_heap(begin, dest):
                nonlocal graph, visited, VAL_INF, KEY_INF
                heap = []
                heappush(heap, (begin, 0))
                dist = [VAL_INF] * (cities + 1)
                dist[begin] = 0
                while heap:
                    idx_curr, cost_curr = heappop(heap)
                    for idx_adj, cost_adj in enumerate(graph[idx_curr]):
                        cost_total = cost_curr + cost_adj
                        if dist[idx_adj] > cost_total:
                            dist[idx_adj] = cost_total
                            heappush(heap, (idx_adj, cost_total))
                return dist[dest]

            def dijkstra(begin, dest):
                nonlocal graph, visited, VAL_INF, KEY_INF
                q = deque([begin])
                # distance from begin to i-th index
                dist = [VAL_INF] * (cities + 1)
                dist[begin] = 0
                # for i in range(cities - 1):
                while q:
                    curr = q.popleft()
                    visited[curr] = True
                    
                    # find unvisited nodes from adjacent of graph[curr]
                    # from unvisited nodes, find the minimum value
                    # "what if there are multiple minimum values?"
                    val_min, key_min = VAL_INF, KEY_INF
                    keys = []
                    for i_adj, adj in enumerate(graph[curr]):
                        # adj: distance from curr to i-adj-th index
                        if not visited[i_adj] and adj != VAL_INF:
                            dist[i_adj] = min(dist[i_adj], dist[curr] + adj)
                            if val_min >= dist[i_adj]:
                                val_min = dist[i_adj]
                                keys.append((dist[i_adj], i_adj))
                                # key_min = i_adj
                    # if key_min != KEY_INF:
                    if keys:
                        for key in keys:
                            val_min, key_min = key
                            q.append(key_min)
                return dist[dest]
            answer = dijkstra_heap(depart, dest)
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
        for i in range(5, 5 + 1):
            inputs.append(read_file(f"최소비용 구하기/input{i}.txt"))
            answers.append(int(read_file(f"최소비용 구하기/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()