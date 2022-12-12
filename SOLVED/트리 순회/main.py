import sys, string
input = sys.stdin.readline

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

def main():
    n = int(input())
    atoz = string.ascii_uppercase
    bt = BinaryTree()
    nodes = []
    for i in range(n):
        nodes.append(Node(i))
        nodes[i].item = atoz[i]
    for i in range(n):
        parent, left, right = input().split()
        i_parent = atoz.find(parent)
        if left != ".":
            nodes[i_parent].left = nodes[atoz.find(left)]
        if right != ".":
            nodes[i_parent].right = nodes[atoz.find(right)]

    bt.root = nodes[0]
    print(bt.preorder())
    print(bt.inorder())
    print(bt.postorder())

if __name__ == "__main__":
    main()