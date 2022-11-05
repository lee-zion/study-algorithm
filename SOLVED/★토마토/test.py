import unittest
import pprint
from collections import deque

def read_file(filename):
    file = open(filename, 'r')
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret

def main(input):
    pp = pprint.PrettyPrinter(indent=4)
    # down, up, left, right
    dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
    [COL_MAX, ROW_MAX] = map(int, input[0].split(" "))
    graph = []
    for row in range(ROW_MAX):
        graph.append(list(map(int, input[1+row].split(" "))))
    pp.pprint(graph)

    day = -1

    # is all element 1?
    already_done = True
    for row in range(ROW_MAX):
        if 0 in graph[row]: # 0 exists
            already_done = False
            break
    # Y -> return 0
    if already_done:
        day = 0
        return [str(day)]

    q = deque([])
    for col in range(COL_MAX):
        for row in range(ROW_MAX):
            if graph[row][col] == 1:
                q.append((row, col))
    
    while q:
        (x, y) = q.popleft()
        curr = graph[x][y]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx > ROW_MAX - 1 or ny < 0 or ny > COL_MAX-1:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = curr + 1
                q.append((nx, ny))
    
    # HOW TO CHECK whether solution do not exist?
    # 2) After search
    # if un-contaminated tomato exists, return -1
    day = -1
    for row in graph:
        for element in row:
            if element == 0:
                return [str(day)]
        day = max(day, max(row))
    return [str(day-1)]

class TestCases(unittest.TestCase):
    def test_input_txt(self):
        input = read_file('★토마토/input.txt')
        answer = read_file('★토마토/output.txt')
        self.assertEqual(main(input), answer)


if __name__ == '__main__':
    unittest.main()