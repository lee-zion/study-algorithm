import unittest
from traceback import print_exception
import sys
from collections import deque

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
            graph = [list(map(int, input[1+i].split())) for i in range(n)]
            class Shark():
                def __init__(self) -> None:
                    self.pos = None
                    self.size = 2
                    self.stomach = 0
                def move(self, x, y):
                    self.pos = [x, y]
                    return True
                def find(self, graph, visited, dist):
                    q = deque([self.pos])
                    visited[self.pos[0]][self.pos[1]] = True
                    dx = [1, -1, 0, 0]
                    dy = [0, 0, 1, -1]
                    founds = []
                    while q:
                        x, y = q.popleft()
                        for i in range(4):
                            nx = x + dx[i]
                            ny = y + dy[i]
                            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                                continue
                            wasteland = graph[nx][ny]
                            if wasteland > self.size or visited[nx][ny]:
                                continue
                            q.append((nx, ny))
                            dist[nx][ny] = dist[x][y] + 1
                            visited[nx][ny] = True
                            if 0 < wasteland < self.size:
                                founds.append([dist[nx][ny], nx, ny])
                    return sorted(founds, key=lambda x: (x[0], x[1], x[2]))
            shark = Shark()
            
            for row, graph_row in enumerate(graph):
                for col, elem in enumerate(graph_row):
                    if elem == 9:
                        shark.move(row, col)
                        graph[row][col] = 0
                        break
            answer = 0
            while True:
                visited = [[False]*n for _ in range(n)]
                dist = [[0]*n for _ in range(n)]
                founds = shark.find(graph, visited, dist)
                if not len(founds):
                    break
                dist, x, y = founds[0]
                # move
                answer += dist
                # print(f"{x}, {y} : {answer}")
                # eat
                graph[x][y] = 0
                shark.stomach += 1
                if shark.stomach == shark.size:
                    shark.size += 1
                    shark.stomach = 0
                shark.move(x, y)
            answers.append(str(answer))
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
        for i in range(1, 6 + 1):
            inputs.append(read_file(f"아기 상어/input{i}.txt"))
            answers.append(read_file(f"아기 상어/output{i}.txt")[0])
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()