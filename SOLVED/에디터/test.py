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

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    """
    LL의 노드는 0번부터 시작한다

    """
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
            node = Node(data) # duplication is bad in design, but if-elif-else is (little) faster than if, if-else
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
            raise IndexError(f"index {index} is out of range")
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

    
    # def remove(self, index):
    #     """
    #     curr의 next를 삭제한다
    #     단, curr = self.head에서 index만큼 next를 이동한다
    #     """
    #     if index >= self.size:
    #         self.tail = self.tail.prev
    #     elif index == 0:
    #         self.head.next.prev = self.head.next
    #         self.head.next = self.head
    #     else:
    #         curr = self.head
    #         for _ in range(index - 1):
    #             curr = curr.next
    #         if not curr.next.next:
    #             self.tail = curr
    #             curr.next = None
    #         else:
    #             curr.next = curr.next.next
    #             curr.next.prev = curr
    #         # curr.next.next.prev = curr
    #         # curr.next = curr.next.next
    #     self.size -= 1

    def __str__(self):
        curr = self.head
        result = ''
        while curr:
            result += curr.data
            curr = curr.next
        return result

def main(inputs):
    answers = []
    try:
        for input in inputs:
            """
            L: 왼쪽 방향키
            D: 오른쪽 방향키
            B: 백스페이스
            P: 문자입력
            """
            # DEQUE solution
            left = deque([])
            right = deque([])
            str_init, num_cmd = input[:2]
            for c in str_init:
                left.append(c)
            
            for i, cmd in enumerate(input[2:]):
                if cmd[0] == "P":
                    left.append(cmd[-1])
                elif cmd[0] == "B" and left:
                    left.pop()
                elif cmd[0] == "L" and left:
                    right.appendleft(left.pop())
                elif cmd[0] == "D" and right:
                    left.append(right.popleft())
            answer = "".join(left) + "".join(right)
            answers.append([answer])

            # LinkedList solution: TIMEOUT
            # ll = LinkedList()
            # str_init, num_cmd = input[:2]
            # for c in str_init:
            #     ll.append(c)
            # cursor = ll.size
            # for i, cmd in enumerate(input[2:]): # for debug purpose, enumerate is used
            #     if cmd[0] == "P":
            #         ll.insert(cmd[-1], cursor)
            #         cursor += 1
            #     elif cmd[0] == "B":
            #         # cursor 왼쪽의 문자를 삭제하므로 remove(cursor - 1)
            #         if cursor > 0:
            #             ll.remove(cursor - 1)
            #             cursor -= 1
            #     elif cmd[0] == "L":
            #         cursor -= 1
            #         cursor = max(cursor, 0)
            #     elif cmd[0] == "D":
            #         cursor += 1
            #         cursor = min(cursor, ll.size)
            #     else:
            #         raise ValueError(f"CMD have invalid value of {cmd[0]} in {cmd}")
            # answer = ""
            # curr = ll.head
            # while True:
            #     answer += curr.data
            #     if not curr.next:
            #         break
            #     curr = curr.next
            # answers.append([answer])
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
        for i in range(1, 3 + 1):
            inputs.append(read_file(f"에디터/input{i}.txt"))
            answers.append((read_file(f"에디터/output{i}.txt")))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()