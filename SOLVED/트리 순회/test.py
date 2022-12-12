import unittest
from traceback import print_exception
import sys, string


def read_file(filename):
    file = open(filename, "r")
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret


class Node(object):
    def __init__(self, item) -> None:
        self.item = item
        self.left = self.right = None


class BinaryTree(object):
    def __init__(self) -> None:
        self.root = None

    def preorder(self):
        order = ""
        def _preorder(node: Node):
            nonlocal order
            order += node.item
            if node.left:
                _preorder(node.left)
            if node.right:
                _preorder(node.right)
        _preorder(self.root)
        return order

    def inorder(self):
        order = ""
        def _inorder(node: Node):
            nonlocal order
            if node.left:
                _inorder(node.left)
            order += node.item
            if node.right:
                _inorder(node.right)
        _inorder(self.root)
        return order

    def postorder(self):
        order = ""
        def _postorder(node: Node):
            nonlocal order
            if node.left:
                _postorder(node.left)
            if node.right:
                _postorder(node.right)
            order += node.item
        _postorder(self.root)
        return order


def main(inputs):
    answers = []
    ATOZ = string.ascii_uppercase
    # ATOZ = [i for i, c in enumerate(string.ascii_uppercase)]
    try:
        for input in inputs:
            # your code here
            n = int(input[0])
            bt = BinaryTree()
            nodes = []
            for i in range(n):
                nodes.append(Node(i))
                nodes[i].item = ATOZ[i]
            for i in range(n):
                parent, left, right = input[1 + i].split()
                i_parent = ATOZ.find(parent)
                if left != ".":
                    nodes[i_parent].left = nodes[ATOZ.find(left)]
                if right != ".":
                    nodes[i_parent].right = nodes[ATOZ.find(right)]

            bt.root = nodes[0]
            answers.append(bt.preorder())
            answers.append(bt.inorder())
            answers.append(bt.postorder())
        return answers
    except Exception:
        print(
            f"==========================================================================="
        )
        print(f"Failed in the case below")
        print(f"input: {input}")
        exc_info = sys.exc_info()
        print_exception(*exc_info)
        print(
            f"==========================================================================="
        )
        del exc_info


class TestCases(unittest.TestCase):
    def test_input_txt(self):
        inputs, answers = [], []
        for i in range(1, 1 + 1):
            inputs.append(read_file(f"트리 순회/input{i}.txt"))
            answers.append(read_file(f"트리 순회/output{i}.txt"))
        self.assertEqual(main(inputs), answers[0])


if __name__ == "__main__":
    unittest.main()
