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
        dp = [10**5] * (10**5 + 1)
        visited = [False] * (10**5 + 1)
        def bfs(depart):
            nonlocal dp, dest
            destT2 = dest * 2
            dp[depart] = 0
            q = deque([depart])
            while q:
                curr = q.popleft()
                currT2 = curr * 2
                currA1 = curr + 1
                currM1 = curr - 1
                if currT2 <= 10**5 and currT2 <= destT2 and currT2 != curr and not visited[currT2]:
                    # dp[currT2] = dp[curr] + 1
                    dp[currT2] = min(dp[currT2], dp[curr] + 1)
                    visited[currT2] = True
                    q.append(currT2)
                if currA1 <= 10**5 and currA1 <= destT2 and not visited[currA1]:
                    # dp[currA1] = dp[curr] + 1
                    dp[currA1] = min(dp[currA1], dp[curr] + 1)
                    q.append(currA1)
                if currM1 >= 0 and not visited[currM1]:
                    # dp[currM1] = dp[curr] + 1
                    dp[currM1] = min(dp[currM1], dp[curr] + 1)


        if depart >= dest:
            answer.append(depart - dest)
        else:
            bfs(depart)
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