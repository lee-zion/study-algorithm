import unittest

def read_file(filename):
    file = open(filename, 'r')
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret

def main(input):
    # 한번에 1 또는 2개 계단만
    # 연속 3개 계단 금지
    # 마지막은 반드시 밟기
    n_stair = int(input[0])

    stairs = []
    for i in range(n_stair):
        stairs.append(int(input[1+i]))
    
    answer = 0
    steps = [1, 2]
    def dfs(curr, visited, point):
        nonlocal stairs
        if not visited[curr]:
            visited[curr] = True
            point += stairs[curr]
            nonlocal answer
            if curr == len(visited) - 1:
                answer = max(answer, point)
            elif curr < len(visited) - 1:
                # range check
                # curr
                if curr + 2 <= len(visited) - 1:
                    dfs(curr + 2, visited, point)
                    visited[curr+2] = False
                if not visited[curr-1]:
                    dfs(curr + 1, visited, point)
                    visited[curr+1] = False
    visited = [False]*n_stair
    dfs(0, visited, 0)
    visited = [False]*n_stair
    dfs(1, visited, 0)
    
    print(answer)
    return [str(answer)]

class TestCases(unittest.TestCase):
    def test_input_txt(self):
        input = read_file('★계단 오르기/input.txt')
        answer = read_file('★계단 오르기/output.txt')
        self.assertEqual(main(input), answer)


if __name__ == '__main__':
    unittest.main()
