import unittest
from traceback import print_exception
import sys
from collections import deque, defaultdict
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
            """
            find a path from i
            i -> x -> i
            there is no symmetric between i->x and x->i, since it is not bi-direction
            """
            n, m, x = map(int, input[0].split())
            graph = defaultdict(list)
            graph_rev = defaultdict(list)
            for i in range(m):
                depart, dest, cost = map(int, input[1+i].split())
                l = [i[0] for i in graph[depart]]
                if dest in l:
                    idx = l.index(dest)
                    graph[depart][idx] = (dest, min(graph[depart][idx][1], cost))
                else:
                    graph[depart].append((dest, cost))
                
                l_rev = [i[0] for i in graph_rev[dest]]
                if depart in l_rev:
                    idx = l_rev.index(depart)
                    graph_rev[dest][idx] = (depart, min(graph_rev[dest][idx][1], cost))
                else:
                    graph_rev[dest].append((depart, cost))
            
            def dijkstra(begin, graph):
                nonlocal visited
                VAL_INF = 1000001
                heap = []
                heappush(heap, (begin, 0))
                dist = [VAL_INF] * (n+1)
                dist[begin] = 0

                while heap:
                    curr_i, curr_cost = heappop(heap)
                    for adj_i, adj_cost in graph[curr_i]:
                        total_cost = curr_cost + adj_cost
                        if dist[adj_i] > total_cost:
                            dist[adj_i] = total_cost
                            heappush(heap, (adj_i, total_cost))
                return dist[1:]

            visited = [False] * (n + 1)
            to_party = dijkstra(x, graph_rev)
            visited = [False] * (n + 1)
            to_home = dijkstra(x, graph)
            answer = max([i+j for i, j in zip(to_party, to_home)])
            answers.append(answer)

            """
            deque dijkstra
            failed at 9%

            n, m, x = map(int, input[0].split())
            graph = defaultdict(list)
            graph_rev = defaultdict(list)
            for i in range(m):
                depart, dest, cost = map(int, input[1+i].split())
                l = [i[0] for i in graph[depart]]
                if dest in l:
                    idx = l.index(dest)
                    graph[depart][idx] = (dest, min(graph[depart][idx][1], cost))
                else:
                    graph[depart].append((dest, cost))
                
                l_rev = [i[0] for i in graph_rev[dest]]
                if depart in l_rev:
                    idx = l_rev.index(depart)
                    graph_rev[dest][idx] = (depart, min(graph_rev[dest][idx][1], cost))
                else:
                    graph_rev[dest].append((depart, cost))
                
            def dijkstra(begin, graph):
                nonlocal visited, n
                VAL_INF = 1000001
                q = deque([begin])
                dist = [VAL_INF] * (n+1)
                dist[begin] = 0
                while q:
                    curr = q.popleft()
                    visited[curr] = True
                    keys = []
                    val_min = VAL_INF
                    for adj, cost_adj in graph[curr]:
                        if not visited[adj]:
                            dist[adj] = min(dist[adj], dist[curr] + cost_adj)
                            if val_min >= dist[adj]:
                                val_min = dist[adj]
                                keys.append(adj)
                    if keys:
                        for key in keys:
                            q.append(key)
                return dist[1:]

            visited = [False] * (n + 1)
            to_party = dijkstra(x, graph_rev)
            visited = [False] * (n + 1)
            to_home = dijkstra(x, graph)
            answer = max([i+j for i, j in zip(to_party, to_home)])
            answers.append(answer)
            """

            """
            # no-dijkstra
            # failed
            n, m, x = map(int, input[0].split())
            graph = defaultdict(list)
            for i in range(m):
                depart, dest, cost = map(int, input[1+i].split())
                graph[depart].append((dest, cost))
            
            def way_back_home_of(begin):
                nonlocal cost, target
                q = deque([begin])
                
                while q:
                    curr, cost_acc = q.popleft()
                    if cost_acc > cost:
                        cost = cost_acc
                    if curr == target:
                        # party over. go home
                        if curr == begin[0]:
                            break
                        target = begin[0]
                    for adj, adj_cost in graph[curr]:
                        q.append((adj, cost + adj_cost))
            costs = []
            for i in range(1, n+1):
                cost = 0
                target = x
                way_back_home_of((i, 0))
                costs.append(cost)
            answer = max(costs)
            answers.append(answer)
            """

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
        for i in range(3, 3 + 1):
            inputs.append(read_file(f"파티/input{i}.txt"))
            answers.append(int(read_file(f"파티/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()