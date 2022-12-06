import unittest
from traceback import print_exception
import sys, os, psutil

# 53.5 kb -> 136.508 kb 
# ~ 83kb@1,208,900
# 747kb@10,880,100 (정비례)
print = sys.stdout.write

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
        # current process RAM usage
        pid = os.getpid()
        current_process = psutil.Process(pid)
        current_process_memory_usage_as_KB = current_process.memory_info()[0] / 2.**20
        print(f"BEFORE CODE: Current memory KB   : {current_process_memory_usage_as_KB: 9.3f} KB")

        # run code
        for input in inputs:
            # your code here
            answer = [0] * 10_001
            n = int(input[0])
            for i in range(n):
                answer[int(input[1+i])] += 1
            for i in range(1, 10_001):
                if answer[i] != 0:
                    for j in range(answer[i]):
                        # ~ 16 seconds
                        print(str(i) + '\n')
                        # ~ 0.9 seconds
                        answers.append(str(i))
                    # # ~ 0.9 seconds
                    # [answers.append(i) for j in range(answer[i])]
                    # # ~ 14 seconds
                    # [print(i) for j in range(answer[i])]
        # current process RAM usage
        pid = os.getpid()
        current_process = psutil.Process(pid)
        current_process_memory_usage_as_KB = current_process.memory_info()[0] / 2.**20
        print(f"AFTER  CODE: Current memory KB   : {current_process_memory_usage_as_KB: 9.3f} KB")
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
            inputs.append(read_file(f"수 정렬하기 3/input{i}.txt"))
            answers.append(read_file(f"수 정렬하기 3/output{i}.txt"))
        self.assertEqual(main(inputs), answers[0])

if __name__ == '__main__':
    unittest.main()