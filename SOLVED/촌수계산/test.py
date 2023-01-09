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
            INF = 101
            n, m = int(input[0]), int(input[2])
            p1, p2 = map(int, input[1].split())
            parents = defaultdict(list)
            children = defaultdict(list)
            for i in range(m):
                a, b = map(int, input[3+i].split())
                children[a].append(b)
                parents[b].append(a)
            answer = INF
            is_finished = False
            visited = [False] * (n + 1)
            def dfs(depth, curr, end):
                nonlocal answer, parents, children, is_finished, visited

                if is_finished:
                    return
                
                # termination condition
                if curr == end:
                    answer = min(answer, depth)
                    is_finished = True
                    return
                
                # find next point
                if not visited[curr]:
                    visited[curr] = True
                    # curr의 parent 찾기
                    for parent in parents[curr]:
                        if not visited[parent]:
                            dfs(depth + 1, parent, end)
                    # curr의 children 찾기
                    for child in children[curr]:
                        if not visited[child]:
                            dfs(depth + 1, child, end)
        
            def dfs_stack(depth, begin, end):
                nonlocal answer, parents, children
                visited = [False] * (n + 1)
                stack = deque([begin])
                while stack:
                    curr = stack.pop()
                    # termination condition
                    if curr == end:
                        answer = min(answer, depth)
                        break
                    # find next point
                    if not visited[curr]:
                        depth += 1
                        visited[curr] = True
                        # curr의 parent 찾기
                        for parent in parents[curr]:
                            if not visited[parent]:
                                stack.append(parent)
                        # curr의 children 찾기
                        for child in children[curr]:
                            if not visited[child]:
                                stack.append(child)
                    
            def bfs(begin, end):
                nonlocal parents, children
                q = deque([begin])
                visited = [False] * (n + 1)
                while q:
                    curr = q.popleft()
                    if curr == end:
                        break

            dfs(0, p1, p2)
            if answer == INF:
                answer = -1
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
        for i in range(1, 2 + 1):
            inputs.append(read_file(f"촌수계산/input{i}.txt"))
            answers.append(int(read_file(f"촌수계산/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()