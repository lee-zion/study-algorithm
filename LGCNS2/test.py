import unittest
from collections import defaultdict

def read_file(filename):
    file = open(filename, 'r')
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret

def main(k, limits, sockets):
    n = len(sockets)
    graph = defaultdict(list)
    graph_leaf = defaultdict(list)
    power_in_use = [0]*n
    for row, socket in enumerate(sockets):
        for conn in socket:
            if conn == -1:
                power_in_use[row] += k
            elif conn != 0:
                graph[row].append(conn-1)
                graph_leaf[conn-1].append(row)

    # find leaf node
    leafs = []
    for leaf in range(n):
        if leaf not in graph:
            leafs.append(leaf)

    # propagate power usage from leaf node
    for leaf in leafs:
        for parent in graph_leaf[leaf]:
            power_in_use[parent] += power_in_use[leaf]

    for child in graph_leaf:
        if child not in leafs:
            for parent in graph_leaf[child]:
                power_in_use[parent] += power_in_use[child]
    
    # for key in graph:
    #     for adj in graph[key]:
    #         power_in_use[key] += power_in_use[adj]
    
    # def update_powers(curr):
    #     nonlocal leafs, power_in_use, graph
    #     if curr in leafs:
    #         return power_in_use[curr]
    #     for child in graph[curr]:
    #         power_in_use[curr] += power_in_use[child] + update_powers(child)
    # update_powers(0)

    is_overpower = [0] * n
    for leaf in range(n):
        is_overpower[leaf] = power_in_use[leaf] - limits[leaf]
        # if power_in_use[leaf] > limits[leaf]:
        #     is_overpower[leaf] = power_in_use[leaf] - limits[leaf]
    
    answer = 0
    # leaf 치기
    for leaf, op in enumerate(is_overpower):
        # leaf에서 뿐만 아니라 중간 탭이나 root에서도 선을 뽑아야 할 수도 있음! 아닌가? 그런 상황이 있나?
        # 모든 콘센트가 똑같이 k만큼 소비하는데 child에서 빼던 본인한테서 빼던 상관없잖?
        # child에서 다 빼버려도 limit를 넘어서 본인것 1개만 써야할 때
        # -> 그러면 child 1개만 남기는게 맞지 않음? ㅇㅇ 그럴듯
        if op > 0 and leaf in leafs:
            # find x that satisfies
            # op - k*x < limits[tab]
            # x > limits/op/k
            tab_removed, r = divmod(op, k)
            if r != 0:
                tab_removed += 1
            
            answer += tab_removed
            power_in_use[leaf] -= k*tab_removed
            while tab_removed:
                for i, val in enumerate(sockets[leaf]):
                    if val == -1:
                        sockets[leaf][i] = 0
                        tab_removed -= 1
                        break
            # for parent in graph_leaf[leaf]:
            #     power_in_use[parent] -= k*tab_removed

    power_in_use = [0]*n
    for row, socket in enumerate(sockets):
        for conn in socket:
            if conn == -1:
                power_in_use[row] += k
    for leaf in leafs:
        for parent in graph_leaf[leaf]:
            power_in_use[parent] += power_in_use[leaf]
    for child in graph_leaf:
        if child not in leafs:
            for parent in graph_leaf[child]:
                power_in_use[parent] += power_in_use[child]
    
    # leaf 제거만으로 부족하다면?
    # 각자 자신의 power도 줄인다
    for leaf in range(n):
        is_overpower[leaf] = power_in_use[leaf] - limits[leaf]
    
    for not_leaf, op in enumerate(is_overpower):
        if op > 0:
            tab_removed, r = divmod(op, k)
            if r:
                tab_removed += 1
            answer += tab_removed
            # while tab_removed:
            #     power_in_use[not_leaf] -= k*tab_removed
            #     for i, val in enumerate(sockets[not_leaf]):
            #         if val == -1:
            #             sockets[not_leaf][i] = 0
            #             tab_removed -= 1
            #             break
    return answer

class TestCases(unittest.TestCase):
    def test_input_txt(self):
        k = 300
        # 테케 변경2: leaf는 limit이 큰데 branch의 limit이 작을 경우
        sockets = [[2, 3, -1, -1, -1], [4, 0, -1, -1, 6], [5, 0, 0, 0, 0], [-1, 0, 0, 0, 0], [-1, -1, -1, -1, -1], [-1, -1, 7, 0, 0], [-1, -1, -1, 0, 0]]
        limits = [2000, 1000, 3000, 200, 600, 500, 2000]
        answer = 10
        # 테케 변형1: chain이 길 경우 deep dive까지 구현이 되어 있는가
        # k = 300
        # sockets = [[2, 3, -1, -1, -1], [4, 0, -1, -1, 6], [5, 0, 0, 0, 0], [-1, 0, 0, 0, 0], [6, 0, 0, 0, 0], [7, 0, 0, 0, 0], [-1, -1, 0, 0, 0]]
        # limits = [2000, 1000, 3000, 200, 600, 500, 500, 500]
        # answer = 7
        # 기본 테케
        # k = 300
        # sockets = [[2, 3, -1, -1, -1], [4, 0, -1, -1, 6], [5, 0, 0, 0, 0], [-1, 0, 0, 0, 0], [-1, -1, -1, -1, -1], [-1, -1, 0, 0, 0]]
        # limits = [2000, 1000, 3000, 200, 600, 500]
        # answer = 7
        self.assertEqual(main(k, limits, sockets), answer)


if __name__ == '__main__':
    unittest.main()