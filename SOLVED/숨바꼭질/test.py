import unittest
from collections import deque

def read_file(filename):
    file = open(filename, 'r')
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret

def main(inputs):
    answer = []
    for input in inputs:
        depart, dest = map(int, input[0].split())
        MAX = 2 * max(depart, dest)
        dp = [0] * (MAX + 1)
        visited = set()
        def bfs(curr, visited):
            nonlocal dest
            q = deque([curr])
            dp[curr] = 0
            visited.add(curr)
            while q:
                v = q.popleft()
                for i in range(3):
                    if i == 0:
                        v_new = v * 2
                    elif i == 1:
                        v_new = v + 1
                    elif i == 2:
                        v_new = v - 1
                    
                    # is index is valid?
                    if v_new > MAX or v_new < 0 or v_new == v or v_new in visited:
                        continue
                    
                    # is distance(v and dest) >= distance(v_new and dest)?
                    # -> append it to the next queue
                    # dist, dist_new = abs(dest - v), abs(dest - v_new)
                    # if dist_new < dist:
                    dp[v_new] = dp[v] + 1 if dp[v_new] == 0 else min(dp[v_new], dp[v] + 1)
                    q.append(v_new)
                    visited.add(v_new)
                    
        if depart >= dest:
            answer.append(depart - dest)
        else:
            bfs(depart, visited)
            answer.append(dp[dest])
    return answer

class TestCases(unittest.TestCase):
    def test_input_txt(self):
        inputs, answers = [], []
        for i in range(1, 6):
            inputs.append(read_file(f'숨바꼭질/input{i}.txt'))
            answers.append(int(read_file(f'숨바꼭질/output{i}.txt')[0]))
        self.assertEqual(main(inputs), answers)
        for i in range(5):
            print(f"{inputs[i]} {answers[i]}")

if __name__ == '__main__':
    unittest.main()