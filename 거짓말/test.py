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
            # party index from 0
            # person index from 1
            n_people, n_party = map(int, input[0].split())
            acquaint = input[1].split()
            n_acquaint = int(acquaint[0])
            parties = [[False]*(n_people + 1) for _ in range(n_party)]
            acquaints = [False] * (n_people + 1)
            for e in list(map(int, acquaint[1:])):
                acquaints[e] = True
            for i_party in range(n_party):
                party = list(map(int, input[2 + i_party].split()))[1:]
                for person in party:
                    parties[i_party][person] = True
            
            # 모든 파티에 대해 <-- acquaint 발생으로 인한 처음에 처리한 파티를 업데이트?
            for party in parties:
                # 파티에 있는 사람 중 acquaint가 있다면
                if True in (party and acquaint):
                    for i, ac in enumerate(acquaint):
                        if ac:
                            party[i] = True
            answer = 0
            for i_party in range(n_party):
                party = parties[i_party]
                can_i_exaggerate = True
                for i in range(n_party):
                    if acquaints[i] and party[i]:
                        can_i_exaggerate = False
                        break
                if can_i_exaggerate:
                    answer += 1
                else:
                    for i in range(n_party):
                        acquaints[i] = acquaints[i] or party[i]
                print("1")

            # n_people, n_party = map(int, input[0].split())
            # acquaints = input[1].split()
            # n_acquaint = int(acquaints[0])
            # if n_acquaint:
            #     acquaints = set(map(int, acquaints[1:]))
            # else:
            #     acquaints = set()
            # parties = []
            # for i in range(n_party):
            #     parties.append(list(map(int, input[2 + i].split()))[1:])
            
            # answer = 0
            # for party in parties:
            #     can_i_exaggerate = True
            #     for attender in party:
            #         if attender in acquaints:
            #             can_i_exaggerate = False
            #             break
                
            #     if can_i_exaggerate:
            #         acquaints.update(party)
            #         answer += 1
            
            # import sys
            # N, M = map(int, input[0].split()) # N은 인원수. M은 파티의 수.
            # truth = list(map(int, input[1].split()))
            # people = {}
            # for i in range(N):
            #     people[i+1] = 0
            # if len(truth) == 1:
            #     None
            # else:
            #     for i in range(1, len(truth)):
            #         people[truth[i]] = 1
            # party = []
            # for i in range(M):
            #     party.append(input[2+i].split())

            # for i in range(len(party)):
            #         party[i] = party[i][1:] # 각파티 정보에서 인원수 정보를 제거함. 
            # cnt = 0
            # rem = []
            # while(True):
            #     cnt = 0
            #     for i in range(len(party)):
            #         for j in range(len(party[i])):
            #             if people[int(party[i][j])] == 1: # 이 파티에 진실을 아는사람이 한명이라도 있다면
            #                 cnt +=1 
            #                 if rem.count(i) == 0:
            #                     rem.append(i) # 진실을 아는 파티는 다음 탐색에서 제거하기 위해 넣어놓음.
            #                     for man in party[i]: # 이 파티의 사람들은 모두 진실을 안다. 
            #                         people[int(man)] = 1
            #     if cnt == 0:
            #         break 
            #     a = len(rem) # 진실을 아는 파티 제거
            #     for i in range(a):
            #         party.remove(party[rem.pop()])
            # answer = len(party)

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
        for i in range(4, 7 + 1):
            inputs.append(read_file(f"거짓말/input{i}.txt"))
            answers.append(int(read_file(f"거짓말/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()