import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.size += 1

    def insert(self, data, index):
        if index >= self.size:
            self.append(data)
            return
        elif index == 0:
            node = Node(data)
            self.head.prev = node
            node.next = self.head
            self.head = node
        else:
            node = Node(data)
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            node.next = curr.next
            curr.next.prev = node
            curr.next = node
            node.prev = curr
        self.size += 1

    def remove(self, index):
        if index >= self.size:
            return
        elif index == 0:
            self.head = self.head.next
            self.head.prev = None
        elif index == self.size - 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next
            curr.next.prev = curr
        self.size -= 1

def main():
    str_init = sys.stdin.readline().strip()
    num_cmd = int(sys.stdin.readline())

    cmds = []
    for _ in range(num_cmd):
        cmds.append(sys.stdin.readline().strip())
    
    ll = LinkedList()
    for c in str_init:
        ll.append(c)
    
    cursor = ll.size
    for cmd in cmds:
        c = cmd[0]
        if c == "P":
            ll.insert(cmd[-1], cursor)
            cursor += 1
        elif c == "B":
            if cursor > 0:
                ll.remove(cursor - 1)
                cursor -= 1
        elif c == "L":
            cursor -= 1
            cursor = max(cursor, 0)
        elif c == "D":
            cursor += 1
            cursor = min(cursor, ll.size)
    answer = ""
    curr = ll.head
    while True:
        if not curr:
            break
        answer += curr.data
        curr = curr.next
    print(answer)
if __name__ == "__main__":
    main()