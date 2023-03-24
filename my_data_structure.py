class MyDataStructure:
    def __init__(self, name: str, type) -> None:
        self.name = name
        self.type = type

class Tree:
    def __init__(self, n) -> None:
        """
        n: number of node
        """
        self.root = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
    
    def find(self, x):
        """
        description
        root node represent the subset

        args
            x: int
            index of node
        
        return
            index of root node
        """
        rx = self.root[x]
        if rx != x:
            return self.find(rx)
        else:
            return x
    
    def compressed_find(self, x):
        """
        description
        similar to Tree.find, except tree path compression
        tree path compression is 

        args
            x: int
            index of node
        
        return
            index of root node
        """
        rx = self.root[x]
        if rx != x:
            self.root[x] = self.find(rx)
            return self.root[x]
        else:
            return x
    
    def union(self, x, y):
        """
        
        """
