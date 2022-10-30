import unittest
from collections import deque
import pprint
pp = pprint.PrettyPrinter(indent=4)

def read_file(filename):
    file = open(filename, 'r')
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret

def main(input):
    T = input[0]
    idx_MNK = [1, 19, 21]
    answer = []
    # down 
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for t in range(int(T)):
        [ROW_MAX, COL_MAX, K] = map(int, input[idx_MNK[t]].split(" "))
        graph = [[0 for _ in range(COL_MAX)] for _ in range(ROW_MAX)]
        visited = [[0 for _ in range(COL_MAX)] for _ in range(ROW_MAX)]
        cnt = 0
        for i in range(K):
            [x, y] = list(map(int, input[idx_MNK[t]+1+i].split(" ")))
            graph[x][y]= 1

        for row in range(ROW_MAX):
            for col in range(COL_MAX):
                try:
                    if graph[row][col] and not visited[row][col]:
                        visited[row][col] = 1
                        cnt += 1
                        q = deque()
                        q.append((row, col))
                        while q:
                            r, c = q.popleft()
                            for i in range(4):
                                qr = r + dx[i]
                                qc = c + dy[i]
                                if qr > ROW_MAX-1 or qc > COL_MAX-1 or qr < 0 or qc < 0:
                                    continue
                                if graph[qr][qc] and not visited[qr][qc]:
                                    visited[qr][qc] = 1
                                    q.append((qr, qc))
                            
                except IndexError:
                    print(row, col)
        answer.append(str(cnt))
    print(answer)
    return answer

class TestCases(unittest.TestCase):
    def test_input_txt(self):
        input = read_file('유기농 배추/input.txt')
        answer = read_file('유기농 배추/output.txt')
        self.assertEqual(main(input), answer)


if __name__ == '__main__':
    unittest.main()
# import unittest
# from collections import deque
# import pprint
# pp = pprint.PrettyPrinter(indent=4)

# def read_file(filename):
#     file = open(filename, 'r')
#     ret = file.readlines()
#     for i, l in enumerate(ret):
#         ret[i] = l.strip()
#     file.close()
#     return ret

# def main(input):
#     # T = input[0]
#     [M, N, K] = map(int, input[1].split(" "))
#     graph = [[0 for _ in range(N)] for _ in range(M)]
#     visited = [[0 for _ in range(N)] for _ in range(M)]
#     answer = 0
#     for i in range(K):
#         [x,y] = list(map(int, input[2+i].split(" ")))
#         graph[x][y]= 1

#     for row in range(M):
#         for col in range(N):
#             try:
#                 if graph[row][col] != visited[row][col]:
#                     visited[row][col] = 1
#                     answer += 1
#                     q = deque([row, col])
#                     while q:
#                         qr = q.popleft()
#                         qc = q.popleft()
#                         # mark all the adjacents as visited
                        
#                         # is downward not visited?
#                         if qr < N-1: # if downward exist
#                             if graph[qr+1][qc] and not visited[qr+1][qc]:
#                                 visited[qr+1][qc] = 1
#                                 # check the all adj of this node
#                                 q.append((qr+1, qc))
#                                 q.append((qr, qc+1))
#                                 q.append((qr, qc-1))
#                                 # q.append(qr+1)
#                                 # q.append(qc)
#                                 # # q.append([qr-1, qc])
#                                 # q.append(qr)
#                                 # q.append(qc+1)
#                                 # q.append(qr)
#                                 # q.append(qc-1)
                        
#                         # is rightside not visited?
#                         if qc < M-1: # if rightside exist
#                             if graph[qr][qc+1] and not visited[qr][qc+1]:
#                                 visited[qr][qc+1] = 1
#                                 q.append(qr+1)
#                                 q.append(qc)
#                                 q.append(qr-1)
#                                 q.append(qc)
#                                 q.append(qr)
#                                 q.append(qc+1)
#                                 # q.append([qr, qc-1])
                        
#                         # is upward not visited?
#                         if qr > 0: # if upside exist
#                             if graph[qr-1][qc] and not visited[qr-1][qc]:
#                                 visited[qr-1][qc] = 1
#                                 # q.append([qr+1, qc])
#                                 q.append(qr-1)
#                                 q.append(qc)
#                                 q.append(qr)
#                                 q.append(qc+1)
#                                 q.append(qr)
#                                 q.append(qc-1)
                        
#                         # is leftside not visited?
#                         if qc > 0: # if leftside exist
#                             if graph[qr][qc-1] and not visited[qr][qc-1]:
#                                 visited[qr][qc-1] = 1
#                                 q.append(qr+1)
#                                 q.append(qc)
#                                 q.append(qr-1)
#                                 q.append(qc)
#                                 q.append(qr)
#                                 q.append(qc-1)
#                                 # q.append([qr, qc+1])
#             except IndexError:
#                 print(row, col)


#     pp.pprint(visited)
#     print(answer)
#     # get connected

#     return True

# class TestCases(unittest.TestCase):
#     def test_input_txt(self):
#         input = read_file('유기농 배추/input.txt')
#         answer = read_file('유기농 배추/output.txt')
#         self.assertEqual(main(input), answer)


# if __name__ == '__main__':
#     unittest.main()