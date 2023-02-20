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
            """
            mkalb: 없으면 dir 생성, 이미 있으면 "duplicated album name" 출력
            rmalb: "삭제된 앨범의 개수, 사진의 개수" 출력
            insert: 없으면 사진 생성, 이미 있으면 "duplicated photo name" 출력
            delete: 삭제된 사진의 개수 출력
            ca: 현재 앨범 이름 출력
            album = {
                name: String
                parent: String (parent album name)
            }
            """
            head = "album"
            class Directory:
                def __init__(self, name: str) -> None:
                    self.name = name
                    self.parent = None
                    self.subdir = set()
                    self.subdir_cnt = 0
                    self.file = set()
                    self.file_cnt = 0
                
                def get_subdirectory(self):
                    return self.subdir
                
                def set_parent(self, parent):
                    self.parent = parent
                
                def add_subdir(self, directory):
                    self.subdir.add(directory)
            
            class Program:
                def __init__(self) -> None:
                    root = Directory("album")
                    self.top = root
                    self.head = root

                def mkdir(self, arg):
                    head = self.head
                    if arg in head.get_subdirectory():
                        print("duplicated album name")
                        return None
                    temp = Directory(arg)
                    temp.set_parent(head)
                    
                    head.add_subdir(temp)
                    head.subdir_cnt += 1
                    
                    while head.parent:
                        head = head.parent
                        head.subdir_cnt += 1
                    
            
            n_command = int(input[0])
            program = Program()
            for i in range(n_command):
                cmd, arg = input[1+i].split()
                if cmd == "mkalb":
                    program.mkdir(arg)

            # answers.append(answer)
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
            inputs.append(read_file(f"앨범정리/input{i}.txt"))
            answers.append(read_file(f"앨범정리/output{i}.txt"))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()