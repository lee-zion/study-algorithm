import unittest
from traceback import print_exception
import sys

def read_file(filename):
    file = open(filename, 'r')
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret

class Tree():
    def __init__(self, n) -> None:
        self.root = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]

    def find(self, x):
        rx = self.root[x]
        if rx == x:
            return x
        else:
            return self.find(rx)
    
    def compression_find(self, x):
        rx = self.root[x]
        if rx == x:
            return x
        else:
            self.root[x] = self.compression_find(rx)
            return self.root[x]

    def union(self, x, y):
        """
        union y to x
        """
        rx, ry = self.find(x), self.find(y)
        if rx > ry:
            self.root[rx] = ry
        elif ry > rx:
            self.root[ry] = rx

    def size_rank_union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        
        if self.rank[ry] > self.rank[rx]:
            rx, ry = ry, rx

        self.root[ry] = rx
        self.rank[rx] += self.rank[ry]
    
    def height_rank_union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        
        if self.rank[ry] > self.rank[rx]:
            rx, ry = ry, rx

        self.root[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
    
    def print_tree(self):
        print(" ".join(map(str, self.root)))

def main(inputs):
    answers = []
    try:
        for input in inputs:
            # your code here
            answer = []
            n, m = map(int, input[0].split())
            tree = Tree(n+1)
            tree.print_tree()
            for i in range(m):
                op, a, b = map(int, input[1+i].split())
                if op: # op == 1
                    answer.append("YES" if tree.compression_find(a) == tree.compression_find(b) else "NO")
                else: # op == 0
                    tree.height_rank_union(a, b)
                tree.print_tree()
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
        for i in range(1, 4 + 1):
            inputs.append(read_file(f"집합의 표현/input{i}.txt"))
            answers.append(read_file(f"집합의 표현/output{i}.txt"))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()