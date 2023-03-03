import unittest
from traceback import print_exception
import sys
from collections import deque
# from string import ascii_lowercase, ascii_uppercase

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
            """
            how to "efficiently" check whether unlocking certain door is mandatory or not?
            
            1) snapshot lock-unlock
            1-1) if unlock is solvable, it is more short path
            1-2) if unlock is unsolvable, we must unlock the locked
            --> how to "efficiently" check which snapshot is the closest to the corresponding key?
            ---> snapshot?

            2) find every path

            application)
            f0.F..1
            ->
            initial path = 0.F..1
            we should have f between 0 and F
            ->
            find f
            0f0.F..1
            (or 0f..F..1)
            ->
            answer = len(0f0.F..1) (= 7)

            application)
            ....1
            #1###
            .1.#0
            ....A
            .1.#.
            0A...1 (중복 4개)
            ->
            initial path 0A...1
            we should have a between 0 and A
            -> 
            find a
            there is no a in maze
            -> 
            -1

            app)
            a#c#eF.1
            .#.#.#..
            .#B#D###
            0....F.1
            C#E#A###
            .#.#.#..
            d#f#bF.1

            0....F.1
            0....D.eF.1
            0....A.bF.1


            -----
            graph traversal problem technique)
            consider begin as node 0, and every key, door, exit are also individual node
            updating minimal distance can solve the problem?
            get minimum distance from begin to all other nodes
            -> 

            [begin->begin, begin->key a, ..., begin->key f, begin->door A, ..., begin->door F, exit 1, ..., exit k]
            """
            maze = []
            WALL, EMPTY = -1, 0
            begin, doors, keys, exit = None, [], [], None
            row, col = map(int, input[0].split())
            for x in range(row):
                temp = []
                for y, s in enumerate(input[1+x]):
                    if s == ".":
                        temp.append(EMPTY)
                    elif s == "#":
                        temp.append(WALL)
                    elif s == "1":
                        temp.append(9)
                    elif s == "0":
                        begin = (x, y, -1)
                        temp.append(EMPTY)
                    elif s in "ABCDEF":
                        temp.append("ABCDEF".find(s) + 2)
                        doors.append((x, y))
                    elif s in "abcdef":
                        temp.append("abcdef".find(s) + 12)
                        keys.append((x, y))
                maze.append(temp)
            
            q = deque([begin])
            dx = [1, 0, -1, 0]
            dy = [0, 1, 0, -1]
            while q:
                x, y, time = q.popleft()
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if nx < 0 or nx >= row or ny < 0 or ny >= col:
                        continue
                    if maze[nx][ny] == WALL:
                        continue

                
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
        for i in range(1, 8 + 1):
            inputs.append(read_file(f"달이 차오른다, 가자./input{i}.txt"))
            answers.append(int(read_file(f"달이 차오른다, 가자./output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()