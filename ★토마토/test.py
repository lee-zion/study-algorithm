import unittest
import pprint
from collections import deque
pp = pprint.PrettyPrinter(indent=4)
def read_file(filename):
    file = open(filename, 'r')
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret

def main(input):
    # down, up, left, right
    dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
    [COL_MAX, ROW_MAX] = map(int, input[0].split(" "))
    graph = []
    visited = [ [0]*COL_MAX for _ in range(ROW_MAX)]
    for row in range(ROW_MAX):
        graph.append(list(map(int, input[1+row].split(" "))))
    pp.pprint(graph)
    # for row in range(M):

    # answer = 0
    answer = 0

    # is all element 1?
    already_done = True
    for row in range(ROW_MAX):
        if not all(graph[row]):
            already_done = False

    # Y -> return 0
    if already_done:
        return answer
    
    # N -> contaminate over iteration
    q = deque([])
    for col in range(COL_MAX):
        for row in range(ROW_MAX):
            if graph[row][col]:
                q.append((row, col))
    # find all 1, contaminate the adjacent
    # answer += 1
    while q:
        (x, y) = q.popleft()



    return True

class TestCases(unittest.TestCase):
    def test_input_txt(self):
        input = read_file('★토마토/input.txt')
        answer = read_file('★토마토/output.txt')
        self.assertEqual(main(input), answer)


if __name__ == '__main__':
    unittest.main()