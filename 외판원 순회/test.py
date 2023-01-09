import unittest
from traceback import print_exception
import sys

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
            n = int(input[0])
            graph = []
            for i in range(n):
                graph.append(list(map(int, input[1+i].split())))
            # dp[curr][visited]
            # curr             : current city index
            # visited          : bitmask of current visit
            # dp[curr][visited]: minimum cost required to return begin after visiting all nonvisited cities
            # DP_INIT = -1
            DP_INIT = n**2 * 10**6 + 1
            VISITED_INIT = 0
            ALL_VISITED = (1 << n) - 1
            dp = [[DP_INIT] * (1 << n) for _ in range(n)]
            
            def dfs(curr, visited):
                nonlocal graph, begin, DP_INIT, ALL_VISITED
                if visited == ALL_VISITED:
                    return graph[curr][begin] if graph[curr][begin] else DP_INIT
                if dp[curr][visited] != DP_INIT:
                    return dp[curr][visited]
                
                for adj in range(n):
                    # if adj == curr:
                    #     continue
                    if not graph[curr][adj]:
                        continue
                    if visited & (1 << adj):
                        continue

                    # dp[curr][visited] = min(dp[curr][visited], dfs(adj, visited | (1 << adj)) + graph[curr][adj]) if dp[curr][visited] != DP_INIT else dfs(adj, visited | (1 << adj)) + graph[curr][adj]
                    dp[curr][visited] = min(dp[curr][visited], dfs(adj, visited | (1 << adj)) + graph[curr][adj])
                return dp[curr][visited]
            for i in range(n):
                begin = i
                answer = dfs(begin, VISITED_INIT)
                if answer != DP_INIT:
                    break
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
            inputs.append(read_file(f"외판원 순회/input{i}.txt"))
            answers.append(int(read_file(f"외판원 순회/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()