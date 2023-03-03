import unittest
from traceback import print_exception
import sys
from collections import deque
from itertools import permutations

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
            col, row = map(int, input[0].split())
            symbol = {
                ".": 0,
                "#": -1,
                "S": 1,
                "X": 2,
                "E": 3
            }
            house = []
            begin, target_list, exit = None, [], None
            for x in range(row):
                temp = []
                for y, s in enumerate(input[1+x]):
                    s_parsed = symbol[s]
                    temp.append(s_parsed)
                    if s_parsed == 2:
                        target_list.append((x, y))
                        continue
                    elif s_parsed == 1:
                        begin = (x, y, 0)
                        continue
                    elif s_parsed == 3:
                        exit = (x, y)
                        continue
                house.append(temp)
            def get_closest_item_from(x, y, flags, goal):
                """
                1) 가장 거리가 멀 것
                2) 출구로부터 거리가 멀 것
                3) 근처에 가까운 물건들이 더 많을 것 -> 귀찮아...
                4) 무작위
                """
                dist = []
                for flag in flags:
                    dist.append(abs(flag[0] - x) + abs(flag[1] - y))
                m = min(dist)
                if dist.count(m) == 1:
                    return flags[dist.index(m)]
                else:
                    mins = [i == m for i in dist]
                    dist2 = []
                    for i, flag in enumerate(flags):
                        if mins[i]:
                            dist2.append(abs(goal[0] - flag[0]) + abs(goal[1] - flag[1]))
                    M = max(dist2)
                    return flags[dist2.index(M)]
            
            # TODO: begin -> targets -> exit
            # target에 대한 heuristic을 써야하나?
            # 아니면 target 하나가 끝나기 전까지만 visited를 두고 하나 끝나면 다시 갱신? -> 이거로 ㄱ
            # 아니면, 모든 path combination 확인해서 minumum 반환하기 -> 위에거랑 exclusive한 개념이 아니니까 같이 구현 ㄱ
            # path1: target1 -> target2 -> ... -> target n -> exit
            # path2: target2 -> target1 -> ... -> target n -> exit
            # ...
            # 잡기술 말고 그냥 모든 조합 완전탐색 하자..

            def get_next_target(target, i, exit):
                l = len(target)
                if i < l:
                    return target[i]
                return exit


            dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
            INF = 2500
            answer = INF

            comb = permutations(target_list, len(target_list))
            for target in comb:
                q = deque([begin])
                x, y, _ = begin
                visited = [[False] * col for _ in range(row)]
                visited[x][y] = True
                ti = 0
                target = list(target)
                print("-"*40)
                print(target)
                # dest = get_closest_item_from(x, y, target, exit) if target else exit
                dest = get_next_target(target, ti, exit)
                while q:
                    x, y, time = q.popleft()
                    print(f"x: {x}   y: {y}   time: {time}")
                    print(f"q: {q}")
                    if (x, y) == dest:
                        if dest == exit:
                            break
                        # target.remove((x, y))
                        ti += 1
                        # if target:
                            # dest = get_closest_item_from(x, y, target, exit)
                        # else:
                        #     dest = exit
                        dest = get_next_target(target, ti, exit)
                        visited = [[False] * col for _ in range(row)]
                        visited[x][y] = True
                        print(f"New start from ({x}, {y}) to {dest}")
                        print(f"Left: {target}")
                        q.clear()

                    for i in range(4):
                        nx, ny = x + dx[i], y + dy[i]
                        if nx < 0 or nx >= row or ny < 0 or ny >= col:
                            continue
                        if visited[nx][ny]:
                            continue
                        if house[nx][ny] < 0:
                            continue
                        q.append((nx, ny, time + 1))
                        visited[nx][ny] = True
                answer = min(answer, time)
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
        for i in range(3, 3 + 1):
            inputs.append(read_file(f"아맞다우산/input{i}.txt"))
            answers.append(int(read_file(f"아맞다우산/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()