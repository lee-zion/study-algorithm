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

def main(inputs):
    answers = []
    try:
        for input in inputs:
            # your code here
            # initial solution; python3 timeout, pypy3 420ms
            # X_MAX, Y_MAX, block = map(int, input[0].split())
            # lands = []
            # for i in range(X_MAX):
            #     land = list(map(int, input[1+i].split()))
            #     lands.append(land)
            # min_global = min([min(row) for row in lands])
            # max_global = max([max(row) for row in lands])
            # costs = []
            # targets = range(min_global, max_global + 1)
            # for target in targets:
            #     cost, block_needed = 0, 0
            #     for lands_row in lands:
            #         for land in lands_row:
            #             diff = land - target
            #             block_needed -= diff
            #             cost = cost + diff * 2 if diff > 0 else cost - diff
            #     if block >= block_needed:
            #         costs.append((cost, target))
            #     else:
            #         break
            # min_cost, max_height_minused = min([(cost, -height) for cost, height in costs])
            # answers.append([f"{min_cost} {-max_height_minused}"])
            # 
            # referenced solution; 
            X_MAX, Y_MAX, block = map(int, input[0].split())
            BLOCK_MAX = 256
            blocks = [0]*(BLOCK_MAX + 1)
            for i in range(X_MAX):
                for e in map(int, input[1+i].split()):
                    blocks[e] += 1
            # land 내 전체 block 갯수
            block_sum = sum(i*blocks[i] for i in range(BLOCK_MAX + 1))
            # 전체 block을 캐내 높이를 0으로 만들 경우에 소요되는 시간을 초기값으로 설정
            answer = (block_sum * 2, 0)
            # land 전체에 1 block씩 더할 경우 필요한 시간
            subtract_one_for_all = X_MAX * Y_MAX
            # 현재 target 달성을 위해 필요한 block 갯수. 전부 캐내니까 초기값을 0으로 설정
            block_needed = 0
            # ??
            acc = blocks[0]
            for i in range(1, BLOCK_MAX + 1):
                # 필요한
                block_needed += acc
                block_sum -= subtract_one_for_all - acc
                acc += blocks[i]
                if block_needed > block_sum + block:
                    break
                else:
                    answer = min(answer, (block_needed + block_sum * 2, -i))
            answers.append([f"{answer[0]} {-answer[1]}"])

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
        for i in range(1, 15 + 1):
            inputs.append(read_file(f"마인크래프트/input{i}.txt"))
            answers.append(read_file(f"마인크래프트/output{i}.txt"))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()